"""Launcher script for Pipefy MCP Server configured for Gemini Enterprise & Antigravity.

Ensures:
1. Dynamic Cloud Run port binding via $PORT.
2. StreamableHTTP transport via `--profile remote` or `--transport http`.
3. Toolset filtering (<100 tools) via PIPEFY_MCP_TOOLSETS.
"""

from __future__ import annotations

import logging
import os
import subprocess
import sys
from dotenv import load_dotenv

# Load local .env if present
load_dotenv()

logging.basicConfig(
    level=os.getenv("LOG_LEVEL", "INFO"),
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger("pipefy_mcp_runner")


def main() -> None:
    host = os.getenv("HOST", "0.0.0.0")
    port = os.getenv("PORT", "8080")
    toolsets = os.getenv("PIPEFY_MCP_TOOLSETS", "cards,pipes,tables")

    # Enforce toolset filtering in environment for Gemini Enterprise compliance
    os.environ["PIPEFY_MCP_TOOLSETS"] = toolsets

    # Check authentication presence
    has_token = bool(os.getenv("PIPEFY_TOKEN"))
    has_sa = bool(
        os.getenv("PIPEFY_SERVICE_ACCOUNT_CLIENT_ID")
        and os.getenv("PIPEFY_SERVICE_ACCOUNT_CLIENT_SECRET")
    )

    if not has_token and not has_sa:
        logger.warning(
            "Neither PIPEFY_TOKEN nor PIPEFY_SERVICE_ACCOUNT credentials were found in the environment. "
            "Please configure credentials in .env or Cloud Run environment variables."
        )
    else:
        auth_mode = "Service Account" if has_sa else "Personal Access Token"
        logger.info("Pipefy authentication mode configured: %s", auth_mode)

    use_stdio = "--stdio" in sys.argv

    if use_stdio:
        logger.info("Starting Pipefy MCP Server in local STDIO mode for Antigravity/CLI...")
        cmd = [
            sys.executable,
            "-m",
            "pipefy_mcp.main",
        ]
    else:
        logger.info("Starting Pipefy MCP Server on %s:%s with toolsets='%s'...", host, port, toolsets)
        cmd = [
            sys.executable,
            "-m",
            "pipefy_mcp.main",
            "--profile",
            "remote",
            "--transport",
            "http",
            "--host",
            host,
            "--port",
            port,
        ]

    try:
        sys.exit(subprocess.call(cmd))
    except KeyboardInterrupt:
        logger.info("Server terminated by user.")
        sys.exit(0)


if __name__ == "__main__":
    main()
