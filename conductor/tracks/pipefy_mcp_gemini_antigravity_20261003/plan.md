# Implementation Plan: Pipefy MCP Server for Gemini Enterprise & Antigravity

## Phase 1: Environment & Scaffolding
- [ ] Task: Setup Project Dependencies and Configuration
    - [ ] Create `pyproject.toml` with `pipefy-mcp-server` and dependencies
    - [ ] Create `.env.example` with Pipefy credentials and toolset configs
    - [ ] Create `docker-compose.yml` for local containerized testing
- [ ] Task: Build Optimized Dockerfile
    - [ ] Create production-ready `Dockerfile` (Python 3.11-slim, StreamableHTTP entrypoint, $PORT dynamic binding)
- [ ] Task: Conductor - User Manual Verification 'Environment & Scaffolding' (Protocol in workflow.md)

## Phase 2: Server Implementation & Verification Tooling
- [ ] Task: Configure Pipefy MCP Server & Toolsets
    - [ ] Create server launcher wrapper `src/run_server.py` ensuring host/port and `PIPEFY_MCP_TOOLSETS` enforcement
    - [ ] Validate toolset filtering keeping active tools below 100
- [ ] Task: Create MCP Client Test Script
    - [ ] Implement `scripts/test_mcp_client.py` for testing JSON-RPC `initialize`, `tools/list`, and call tool against StreamableHTTP endpoint
    - [ ] Verify local execution against mock or live credentials
- [ ] Task: Conductor - User Manual Verification 'Server Implementation & Verification Tooling' (Protocol in workflow.md)

## Phase 3: Integration & Deployment Guides
- [ ] Task: Cloud Run Deployment Automation
    - [ ] Create `deploy_cloud_run.ps1` and `deploy_cloud_run.sh` for one-click deployment to Google Cloud Run free tier
- [ ] Task: Setup & Portfolio Documentation
    - [ ] Create `docs/GEMINI_ENTERPRISE_SETUP.md` (Connecting Custom MCP Data Store in Vertex AI / Gemini Enterprise)
    - [ ] Create `docs/ANTIGRAVITY_SETUP.md` (Configuring Antigravity MCP integration for free local use)
    - [ ] Update root `README.md` showcasing the project architecture for portfolio
- [ ] Task: Conductor - User Manual Verification 'Integration & Deployment Guides' (Protocol in workflow.md)
