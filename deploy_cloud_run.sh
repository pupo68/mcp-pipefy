#!/usr/bin/env bash
# ==============================================================================
# Google Cloud Run Deployment Script (Bash / Linux / macOS)
# Zero-Cost Configuration: Uses Google Cloud Run Free Tier (Scale-to-Zero)
# ==============================================================================

set -euo pipefail

REGION="${REGION:-us-central1}"
SERVICE_NAME="${SERVICE_NAME:-pipefy-mcp-server}"
PROJECT_ID="${GOOGLE_CLOUD_PROJECT:-$(gcloud config get-value project 2>/dev/null || echo "")}"

if [ -z "$PROJECT_ID" ]; then
    read -rp "Enter your Google Cloud Project ID: " PROJECT_ID
fi

echo "=========================================================="
echo " Deploying Pipefy MCP Server to Google Cloud Run (Free Tier)"
echo " Project: $PROJECT_ID | Region: $REGION | Service: $SERVICE_NAME"
echo "=========================================================="

# Read credentials from .env if present
ENV_ARGS="PIPEFY_MCP_TOOLSETS=cards,pipes,tables"
if [ -f .env ]; then
    while IFS= read -r line || [ -n "$line" ]; do
        line=$(echo "$line" | xargs)
        if [[ "$line" =~ ^PIPEFY_[A-Z_]+= ]]; then
            ENV_ARGS="$ENV_ARGS,$line"
        fi
    done < .env
fi

# Deploy with scale-to-zero settings for zero cost
gcloud run deploy "$SERVICE_NAME" \
    --project "$PROJECT_ID" \
    --region "$REGION" \
    --source . \
    --platform managed \
    --allow-unauthenticated \
    --min-instances 0 \
    --max-instances 1 \
    --memory 512Mi \
    --cpu 1 \
    --set-env-vars "$ENV_ARGS"

SERVICE_URL=$(gcloud run services describe "$SERVICE_NAME" --project "$PROJECT_ID" --region "$REGION" --format "value(status.url)")

echo "=========================================================="
echo " DEPLOYMENT SUCCESSFUL!"
echo " Service URL: $SERVICE_URL"
echo " MCP Endpoint for Gemini Enterprise:"
echo "   $SERVICE_URL/mcp"
echo "=========================================================="
