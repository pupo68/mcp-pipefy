# Technology Stack

## 1. Runtime & Core Language
* **Linguagem:** Python 3.11+ (modern typing, asyncio nativo, alta performance para I/O de rede).
* **Gerenciador de Pacotes e Ambiente:** `uv` / `pip` (gerenciamento rápido e determinístico de dependências).

## 2. MCP & Servidor HTTP
* **Framework MCP:** `mcp[cli]==2.0.*` / `pipefy-mcp-server` (baseado no kit oficial [pipefy/ai-toolkit](https://github.com/pipefy/ai-toolkit)).
* **Servidor HTTP:** `Starlette` + `Uvicorn` executando com transporte **StreamableHTTP** (compatibilidade total com a especificação do Gemini Enterprise).
* **Filtragem de Ferramentas:** `PIPEFY_MCP_TOOLSETS` (ex.: `cards,pipes,tables`) para manter as ações ativas abaixo de 100.

## 3. Integração de API (Pipefy)
* **Cliente HTTP/GraphQL:** `httpx` (assíncrono, suporte a streaming e pool de conexões HTTP/2).
* **Endpoint Alvo:** `https://api.pipefy.com/graphql`.
* **Autenticação:** Suporte a Service Account (`client_credentials`) e Personal Bearer Token (`PIPEFY_TOKEN`).

## 4. Containerização & Cloud Deployment
* **Container:** Docker (`python:3.11-slim`), otimizado para inicialização ultrarrápida (cold-start < 2s).
* **Infraestrutura em Nuvem:** Google Cloud Run (100% no tier gratuito: até 2 milhões de requisições/mês, scale-to-zero, terminação TLS automática com CA pública).
* **Integração de Agentes:**
  * **Gemini Enterprise:** Conector Custom MCP Server via StreamableHTTP no Cloud Run.
  * **Antigravity IDE:** Conexão direta local (stdio ou HTTP) integrada ao ambiente de desenvolvimento.
