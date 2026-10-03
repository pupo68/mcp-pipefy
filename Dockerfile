FROM python:3.11-slim

# Avoid buffering and bytecode generation
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PORT=8080 \
    HOST=0.0.0.0

WORKDIR /app

# Install curl and uv for ultra-fast dependency resolution
RUN apt-get update && apt-get install -y --no-install-recommends curl \
    && rm -rf /var/lib/apt/lists/* \
    && pip install --no-cache-dir uv

# Copy dependency definition
COPY pyproject.toml .

# Install dependencies using uv
RUN uv pip install --system --no-cache "pipefy-mcp-server>=0.5.0b0" "httpx>=0.27.0" "starlette>=0.37.0" "uvicorn>=0.30.0" "pydantic>=2.7.0" "python-dotenv>=1.0.0"

# Copy source and scripts
COPY src/ /app/src/

# Cloud Run dynamic port exposure
EXPOSE 8080

# Run the MCP server with StreamableHTTP
CMD ["python", "-m", "src.run_server"]
