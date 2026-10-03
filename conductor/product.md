# Initial Concept

Conectar o Gemini Enterprise e o Antigravity ao Pipefy através do Model Context Protocol (MCP) de maneira 100% gratuita (aproveitando os tiers gratuitos como Google Cloud Run free tier e execução local), estruturando a integração como um projeto de portfólio de engenharia de software e IA.


---

# Product Guide: Pipefy MCP Server (Gemini Enterprise & Antigravity)

## 1. Product Vision
Fornecer um conector de integração baseado no **Model Context Protocol (MCP)** que permite a agentes de IA corporativos (**Google Gemini Enterprise**) e assistentes locais de desenvolvimento (**Google Antigravity**) interagirem de forma autônoma e segura com fluxos de processos do **Pipefy**. O projeto é construído sobre uma arquitetura de custo zero (Cloud Run Free Tier e execução local via stdio) e desenhado como peça de destaque para portfólio de engenharia de software e IA.

## 2. Target Audience & Personas
* **Engenheiros de IA e Desenvolvedores (Portfólio / Hands-on):** Usuários do Antigravity que desejam consultar e automatizar rotinas no Pipefy diretamente de sua IDE sem custos de infraestrutura.
* **Empresas e Usuários Corporativos (Gemini Enterprise):** Agentes de IA corporativos no Google Cloud que demandam ações auditadas e seguras em processos operacionais (Kanban, Helpdesk, Compras, RH, etc.).

## 3. Core Features & Capabilities
* **Integração Dual (Local + Nuvem):**
  - **Local (stdio / StreamableHTTP):** Conexão imediata com o Antigravity IDE.
  - **Nuvem (StreamableHTTP no Google Cloud Run):** Conexão HTTPS com certificado de CA pública para o Gemini Enterprise.
* **Operações de Processos (Pipes & Phases):**
  - Listagem e detalhamento de pipes, fases e campos de formulários.
* **Gestão de Cards e Demandas:**
  - Consulta de cards com filtros por fase ou pipe.
  - Criação de novos cards com preenchimento estruturado de campos.
  - Atualização de status/fases (move card) e valores de campos.
  - Adição de comentários e histórico de auditoria.
* **Bancos de Dados Pipefy (Tables):**
  - Leitura e criação de registros em tabelas/bancos de dados do Pipefy.
* **Custo Zero & Eficiência:**
  - Otimizado para o tier gratuito do Google Cloud Run (scale-to-zero, 2M requisições/mês grátis).
  - Controle de superfície de ferramentas (<100 ações) para máxima precisão de function calling.
