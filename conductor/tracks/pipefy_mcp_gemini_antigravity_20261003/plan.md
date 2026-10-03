# Implementation Plan: Pipefy MCP Server for Gemini Enterprise & Antigravity

## Phase 1: Environment & Scaffolding
- [x] Task: Setup Project Dependencies and Configuration
    - [x] Create `pyproject.toml` with `pipefy-mcp-server` and dependencies
    - [x] Create `.env.example` with Pipefy credentials and toolset configs
    - [x] Create `docker-compose.yml` for local containerized testing
- [x] Task: Build Optimized Dockerfile
    - [x] Create production-ready `Dockerfile` (Python 3.11-slim, StreamableHTTP entrypoint, $PORT dynamic binding)
- [x] Task: Conductor - User Manual Verification 'Environment & Scaffolding' (Protocol in workflow.md)

## Phase 2: Server Implementation & Verification Tooling
- [x] Task: Configure Pipefy MCP Server & Toolsets
    - [x] Create server launcher wrapper `src/run_server.py` ensuring host/port and `PIPEFY_MCP_TOOLSETS` enforcement
    - [x] Validate toolset filtering keeping active tools below 100
- [x] Task: Create MCP Client Test Script
    - [x] Implement `scripts/test_mcp_client.py` for testing JSON-RPC `initialize`, `tools/list`, and call tool against StreamableHTTP endpoint
    - [x] Verify local execution against mock or live credentials
- [x] Task: Conductor - User Manual Verification 'Server Implementation & Verification Tooling' (Protocol in workflow.md)

## Phase 3: Integration & Deployment Guides
- [x] Task: Cloud Run Deployment Automation
    - [x] Create `deploy_cloud_run.ps1` and `deploy_cloud_run.sh` for one-click deployment to Google Cloud Run free tier
- [x] Task: Setup & Portfolio Documentation
    - [x] Create `docs/GEMINI_ENTERPRISE_SETUP.md` (Connecting Custom MCP Data Store in Vertex AI / Gemini Enterprise)
    - [x] Create `docs/ANTIGRAVITY_SETUP.md` (Configuring Antigravity MCP integration for free local use)
    - [x] Update root `README.md` showcasing the project architecture for portfolio
- [x] Task: Conductor - User Manual Verification 'Integration & Deployment Guides' (Protocol in workflow.md)
