# Specification: Pipefy MCP Server for Gemini Enterprise & Antigravity (Zero Cost)

## 1. Overview
Desenvolver, configurar e containerizar o servidor Pipefy Model Context Protocol (MCP) baseado no `pipefy/ai-toolkit`, suportando transporte StreamableHTTP para conexão corporativa com o Gemini Enterprise (Google Cloud Run free tier) e execução local para integração direta com a IDE Antigravity sem custos.

## 2. Functional Requirements
* **FR-01 (Transporte StreamableHTTP & stdio):** Servidor deve operar em modo StreamableHTTP sobre Starlette/Uvicorn (para nuvem/Gemini) e suportar inicialização local para Antigravity.
* **FR-02 (Curadoria de Ferramentas / Toolsets):** Expor ferramentas essenciais de negócio através de `PIPEFY_MCP_TOOLSETS` (`cards,pipes,tables`), garantindo total conformidade com o limite recomendado (<100 ferramentas) do Gemini Enterprise.
* **FR-03 (Operações de Processo & Cards):**
  - Listagem de pipes e fases.
  - Leitura detalhada de cards, campos e comentários.
  - Criação de cards com campos customizados.
  - Movimentação de cards entre fases.
  - Inserção de comentários no histórico do card.
* **FR-04 (Autenticação Flexível):** Suporte a Personal Access Token (`PIPEFY_TOKEN`) e Service Account Corporativa (`CLIENT_ID` + `CLIENT_SECRET`).
* **FR-05 (Scripts de Verificação & Cliente de Teste):** Script de teste em Python para realizar handshake JSON-RPC (`initialize`, `tools/list`) e simular chamadas de ferramentas.

## 3. Non-Functional Requirements
* **NFR-01 (Arquitetura Custo Zero):** Projetado para rodar no Google Cloud Run Free Tier (scale-to-zero, vCPU/RAM sob demanda).
* **NFR-02 (Conformidade TLS):** Executar no Cloud Run sob terminação HTTPS com certificado assinado por CA pública reconhecida pelo Google.
* **NFR-03 (Portfólio Ready):** Documentação clara com instruções de uso local e deploy em nuvem com um clique.

## 4. Acceptance Criteria
1. Servidor sobe em container Docker na porta definida por `$PORT` e responde ao protocolo StreamableHTTP.
2. Script cliente executa handshake MCP com sucesso e lista as ferramentas do Pipefy.
3. Teste de chamada de ferramenta retorna dados reais ou estruturados do Pipefy.
4. Guia passo a passo de registro no console do Gemini Enterprise (Agent Builder) documentado.
