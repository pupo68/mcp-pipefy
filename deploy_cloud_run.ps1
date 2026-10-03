# ==============================================================================
# Google Cloud Run Deployment Script (PowerShell / Windows)
# Zero-Cost Configuration: Uses Google Cloud Run Free Tier (Scale-to-Zero)
# ==============================================================================

[CmdletBinding()]
param(
    [Parameter(Mandatory=$false)]
    [string]$ProjectId = $env:GOOGLE_CLOUD_PROJECT,

    [Parameter(Mandatory=$false)]
    [string]$Region = "us-central1",

    [Parameter(Mandatory=$false)]
    [string]$ServiceName = "pipefy-mcp-server"
)

Write-Host "==========================================================" -ForegroundColor Cyan
Write-Host " Deploying Pipefy MCP Server to Google Cloud Run (Free Tier)" -ForegroundColor Cyan
Write-Host "==========================================================" -ForegroundColor Cyan

# 1. Check gcloud CLI
if (-not (Get-Command gcloud -ErrorAction SilentlyContinue)) {
    Write-Error "Google Cloud SDK ('gcloud') was not found on PATH. Please install from https://cloud.google.com/sdk"
    exit 1
}

# 2. Project ID resolution
if (-not $ProjectId) {
    $ProjectId = gcloud config get-value project 2>$null
}

if (-not $ProjectId) {
    $ProjectId = Read-Host "Enter your Google Cloud Project ID"
}

Write-Host "[*] Target GCP Project: $ProjectId" -ForegroundColor Yellow
Write-Host "[*] Target GCP Region:  $Region" -ForegroundColor Yellow
Write-Host "[*] Service Name:       $ServiceName" -ForegroundColor Yellow

# 3. Read Pipefy credentials from .env if available
$EnvFile = Join-Path $PSScriptRoot ".env"
$PipefyEnvArgs = @()

if (Test-Path $EnvFile) {
    Write-Host "[*] Reading credentials from .env file..." -ForegroundColor Green
    Get-Content $EnvFile | ForEach-Object {
        $line = $_.Trim()
        if ($line -and -not $line.StartsWith("#") -and ($line -match "^(PIPEFY_[A-Z_]+)=(.+)$")) {
            $PipefyEnvArgs += "$($Matches[1])=$($Matches[2])"
        }
    }
}

$EnvVarsString = ($PipefyEnvArgs + @("PIPEFY_MCP_TOOLSETS=cards,pipes,tables")) -join ","

Write-Host "`n[*] Deploying container to Cloud Run with scale-to-zero (0-1 instances)..." -ForegroundColor Cyan

# 4. Deploy to Cloud Run
# Settings configured for 100% free tier coverage:
# - min-instances=0 (scale to zero when idle)
# - max-instances=1 (prevents accidental spikes)
# - memory=512Mi, cpu=1
gcloud run deploy $ServiceName `
    --project $ProjectId `
    --region $Region `
    --source . `
    --platform managed `
    --allow-unauthenticated `
    --min-instances 0 `
    --max-instances 1 `
    --memory 512Mi `
    --cpu 1 `
    --set-env-vars "$EnvVarsString"

if ($LASTEXITCODE -eq 0) {
    $ServiceUrl = gcloud run services describe $ServiceName --project $ProjectId --region $Region --format "value(status.url)"
    Write-Host "`n==========================================================" -ForegroundColor Green
    Write-Host " DEPLOYMENT SUCCESSFUL!" -ForegroundColor Green
    Write-Host " Service URL: $ServiceUrl" -ForegroundColor Green
    Write-Host " MCP Endpoint for Gemini Enterprise:" -ForegroundColor Yellow
    Write-Host "   $ServiceUrl/mcp" -ForegroundColor Cyan
    Write-Host "==========================================================" -ForegroundColor Green
} else {
    Write-Error "Deployment failed. Check the error output above."
}
