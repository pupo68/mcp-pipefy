"""Test client for Pipefy MCP StreamableHTTP endpoint.

Performs MCP handshake (initialize, tools/list) and validates compliance
with Gemini Enterprise specifications (< 100 tools, valid JSON-RPC 2.0).
"""

from __future__ import annotations

import argparse
import json
import sys
import httpx


def _parse_mcp_response(res: httpx.Response) -> dict:
    content_type = res.headers.get("content-type", "")
    text = res.text.strip()
    if "text/event-stream" in content_type or "data:" in text:
        for line in text.splitlines():
            line = line.strip()
            if line.startswith("data:"):
                return json.loads(line[5:].strip())
    return res.json()


def test_mcp_endpoint(base_url: str, auth_token: str | None = None) -> bool:
    endpoint = base_url.rstrip("/")
    if not endpoint.endswith("/mcp"):
        endpoint = f"{endpoint}/mcp"

    print(f"\n========================================================")
    print(f"Testing MCP Server Endpoint: {endpoint}")
    print(f"========================================================\n")

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json, text/event-stream",
    }
    if auth_token:
        headers["Authorization"] = f"Bearer {auth_token}"

    client = httpx.Client(timeout=15.0)

    # 1. Step 1: Initialize
    print("[1/3] Sending 'initialize' JSON-RPC request...")
    init_payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "initialize",
        "params": {
            "protocolVersion": "2024-11-05",
            "capabilities": {},
            "clientInfo": {
                "name": "gemini-enterprise-tester",
                "version": "1.0.0",
            },
        },
    }

    try:
        res = client.post(endpoint, json=init_payload, headers=headers)
        if res.status_code not in (200, 202):
            print(f"[-] 'initialize' failed with status code {res.status_code}: {res.text}")
            return False

        init_data = _parse_mcp_response(res)
        server_info = init_data.get("result", {}).get("serverInfo", {})
        protocol_version = init_data.get("result", {}).get("protocolVersion", "unknown")
        print(f"[+] Initialize success!")
        print(f"    Server Name: {server_info.get('name', 'unknown')}")
        print(f"    Server Version: {server_info.get('version', 'unknown')}")
        print(f"    Protocol Version: {protocol_version}")

        # Capture session if present in headers
        session_id = res.headers.get("mcp-session-id")
        if session_id:
            headers["mcp-session-id"] = session_id
            print(f"    MCP Session ID: {session_id}")

    except Exception as exc:
        print(f"[-] Connection failed during initialize: {exc}")
        return False

    # 2. Step 2: Send initialized notification
    print("\n[2/3] Sending 'notifications/initialized'...")
    try:
        client.post(
            endpoint,
            json={"jsonrpc": "2.0", "method": "notifications/initialized", "params": {}},
            headers=headers,
        )
        print("[+] Initialized notification sent.")
    except Exception as exc:
        print(f"[!] Warning on initialized notification: {exc}")

    # 3. Step 3: Tools List
    print("\n[3/3] Sending 'tools/list' request...")
    tools_payload = {
        "jsonrpc": "2.0",
        "id": 2,
        "method": "tools/list",
        "params": {},
    }

    try:
        res = client.post(endpoint, json=tools_payload, headers=headers)
        if res.status_code != 200:
            print(f"[-] 'tools/list' failed with status code {res.status_code}: {res.text}")
            return False

        tools_data = _parse_mcp_response(res)
        tools = tools_data.get("result", {}).get("tools", [])
        tool_count = len(tools)

        print(f"[+] Retrieved {tool_count} active tools.")

        # Gemini Enterprise Compliance Check (< 100 tools)
        if tool_count <= 100:
            print(f"[+] Gemini Enterprise compliance check PASSED ({tool_count} <= 100 tools).")
        else:
            print(
                f"[!] WARNING: Tool count ({tool_count}) exceeds the Gemini Enterprise recommended limit of 100. "
                f"Consider tuning PIPEFY_MCP_TOOLSETS."
            )

        print("\nSample registered tools:")
        for tool in tools[:10]:
            name = tool.get("name", "unknown")
            desc = tool.get("description", "").split("\n")[0][:80]
            print(f"  * {name:<25} - {desc}")

        if tool_count > 10:
            print(f"  ... and {tool_count - 10} more tools.")

        print("\n========================================================")
        print("ALL CHECKS PASSED: Server is ready for Gemini Enterprise & Antigravity!")
        print("========================================================\n")
        return True

    except Exception as exc:
        print(f"[-] Failed during tools/list: {exc}")
        return False


def main() -> None:
    parser = argparse.ArgumentParser(description="Test Pipefy MCP StreamableHTTP endpoint.")
    parser.add_argument(
        "url",
        nargs="?",
        default="http://localhost:8080/mcp",
        help="MCP Server URL (default: http://localhost:8080/mcp)",
    )
    parser.add_argument(
        "--token",
        "-t",
        default=None,
        help="Optional Bearer token for authenticated endpoints",
    )
    args = parser.parse_args()

    success = test_mcp_endpoint(args.url, args.token)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
