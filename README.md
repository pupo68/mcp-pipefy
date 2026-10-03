# Pipefy MCP Enterprise: Conexão Gemini Enterprise & Antigravity

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/)
[![Model Context Protocol](https://img.shields.io/badge/MCP-2.0%20StreamableHTTP-orange.svg)](https://modelcontextprotocol.io/)
[![Google Cloud Run](https://img.shields.io/badge/Google%20Cloud-Run%20Free%20Tier-4285F4.svg)](https://cloud.google.com/run)
[![License: Apache 2.0](https://img.shields.io/badge/license-Apache%202.0-green.svg)](LICENSE)

Servidor corporativo e de desenvolvimento baseado no **Model Context Protocol (MCP)** para integrar agentes de IA (**Google Gemini Enterprise** e **Google Antigravity**) aos fluxos de trabalho e processos do **Pipefy**.

Construído sobre o kit oficial [`pipefy/ai-toolkit`](https://github.com/pipefy/ai-toolkit) e otimizado com arquitetura de **custo zero** (Google Cloud Run Free Tier com *scale-to-zero* e execução local).

---

## 🏗️ Arquitetura do Sistema

```mermaid
flowchart TD
    subgraph Clients["Clientes MCP Compatíveis"]
        GE["Google Gemini Enterprise<br/>(Vertex AI Agent Platform)"]
        AG["Google Antigravity IDE / CLI<br/>(Ambiente Local)"]
    end

    subgraph Infrastructure["Serviço Pipefy MCP"]
        CR["Google Cloud Run (Free Tier)<br/>(StreamableHTTP / HTTPS com CA Pública)"]
        STD["Processo Local (STDIO / HTTP)<br/>(Desenvolvimento Gratuito)"]
    end

    subgraph PipefyCloud["Plataforma Pipefy"]
        API["Pipefy GraphQL API<br/>https://api.pipefy.com/graphql"]
        Pipes["Pipes, Fases & Formulários"]
        Cards["Cards, Movimentação & Comentários"]
        Tables["Bancos de Dados & Tabelas"]
    end

    GE -->|"StreamableHTTP (POST/SSE)"| CR
    AG -->|"STDIO / Local HTTP"| STD
    CR -->|"GraphQL API (Bearer Auth)"| API
    STD -->|"GraphQL API (Bearer Auth)"| API
    API --> Pipes
    API --> Cards
    API --> Tables
```

---

## 🌟 Principais Destaques

* **Conformidade Total com Gemini Enterprise:**
  * Transporte nativo **`StreamableHTTP`** sobre Starlette e Uvicorn.
  * Terminação HTTPS automática com certificado TLS emitido por CA pública confiável no Cloud Run.
  * Curadoria de ferramentas (`PIPEFY_MCP_TOOLSETS=cards,pipes,tables`) mantendo as ações ativas **abaixo do limite de 100 ferramentas** recomendado pela Google.
* **Integração Gratuita com o Antigravity:**
  * Suporte a modo `--stdio` para rodar localmente sem expor portas.
  * Capacidade de interagir com o Pipefy diretamente nas conversas da IDE.
* **Custo Zero de Infraestrutura:**
  * Otimizado para o tier gratuito do Cloud Run (até 2 milhões de requisições/mês, escala automática para zero instâncias quando inativo).
* **Segurança Corporativa:**
  * Suporte a Service Accounts do Pipefy (`client_credentials`) e Personal Access Tokens.
  * Credenciais injetadas por variáveis de ambiente ou Secret Manager, sem risco de vazamento em código.

---

## 🚀 Como Começar

### 1. Configurar Credenciais Locais
Copie o arquivo de exemplo de ambiente e preencha suas credenciais do Pipefy:
```bash
cp .env.example .env
```
Obtenha seu token em: [app.pipefy.com/tokens](https://app.pipefy.com/tokens) ou via Service Account em *Company Settings*.

### 2. Executar Localmente

#### Modo StreamableHTTP (para testes de API):
```bash
python -m src.run_server
# Servidor ouvindo em http://0.0.0.0:8080/mcp
```

#### Modo STDIO (para integração direta no Antigravity / Claude / Cursor):
```bash
python -m src.run_server --stdio
```

### 3. Validar a Conexão MCP
Execute o script de teste automatizado para validar o handshake JSON-RPC 2.0 e o limite de ferramentas:
```bash
python scripts/test_mcp_client.py http://localhost:8080/mcp
```

---

## ☁️ Deploy no Google Cloud Run (Free Tier)

Para publicar o servidor com certificado TLS válido para o Gemini Enterprise em um clique:

* **No Windows (PowerShell):**
  ```powershell
  .\deploy_cloud_run.ps1
  ```
* **No Linux / macOS (Bash):**
  ```bash
  chmod +x deploy_cloud_run.sh
  ./deploy_cloud_run.sh
  ```

---

## 📚 Guias Detalhados
* 📘 [Conectando ao Google Gemini Enterprise](docs/GEMINI_ENTERPRISE_SETUP.md)
* 📗 [Conectando ao Google Antigravity (Local Gratuito)](docs/ANTIGRAVITY_SETUP.md)
* 📋 [Plano de Arquitetura e Engenharia (PLAN.md)](PLAN.md)
* 🚦 [Contexto e Trilha Conductor](conductor/index.md)
