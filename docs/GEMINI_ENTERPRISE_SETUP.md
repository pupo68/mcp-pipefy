# Conectando o Pipefy MCP Server ao Google Gemini Enterprise

Este guia orienta o registro e a ativação do servidor MCP do Pipefy dentro do **Google Gemini Enterprise** (Vertex AI Agent Builder / Platform).

---

## 1. Pré-requisitos
1. Servidor Pipefy MCP publicado e rodando no **Google Cloud Run** (via `./deploy_cloud_run.ps1` ou `./deploy_cloud_run.sh`).
2. Endpoint HTTPS ativo gerado pelo Cloud Run (exemplo: `https://pipefy-mcp-server-xyz.a.run.app`).
3. Conta com privilégios de edição no console do **Google Cloud / Gemini Enterprise**.

---

## 2. Passo a Passo no Console do Gemini Enterprise

### Passo 1: Acessar a Gestão de Data Stores
1. No [Google Cloud Console](https://console.cloud.google.com/), certifique-se de estar no projeto GCP correto.
2. Navegue até o menu de navegação e selecione **Gemini Enterprise** (ou **Vertex AI Agent Builder**).
3. No menu lateral esquerdo, clique em **Data Stores** (ou **Connected Apps / Connectors**).

### Passo 2: Criar um Novo Data Store MCP Customizado
1. Clique no botão **+ Create Data Store** (ou *New Connector*).
2. Na lista de tipos de conectores disponíveis, selecione **Custom MCP Server**.
3. Preencha os campos de configuração da conexão:
   * **Data Store Name:** `pipefy-processes`
   * **Display Name:** `Pipefy Operational Hub`
   * **MCP Server URL:** Insira a URL HTTPS do Cloud Run com o sufixo `/mcp`:
     ```text
     https://<SEU-SERVICO-CLOUD-RUN>.a.run.app/mcp
     ```
   * **Transport Protocol:** `StreamableHTTP` (o Gemini Enterprise seleciona este transporte por padrão).
   * **Authentication Type:**
     * Se o serviço no Cloud Run estiver aberto (`--allow-unauthenticated`), selecione `No Auth`.
     * Se o serviço for privado, configure a autenticação via `Service Account` / `Google IAM`, concedendo o papel `roles/run.invoker` à conta de serviço do Gemini Enterprise.

### Passo 3: Validação da Conexão
1. Clique em **Test Connection** / **Save**.
2. O Gemini Enterprise enviará um handshake inicial (`initialize` e `tools/list`) para o Cloud Run.
3. Quando a verificação for concluída, o status do Data Store mudará para **Active**.
4. Você verá a lista de ferramentas importadas (ações de cards, pipes, fases e tabelas). Devido à configuração `PIPEFY_MCP_TOOLSETS=cards,pipes,tables`, o total de ferramentas estará estritamente dentro da recomendação de **< 100 ações**.

---

## 3. Vinculando o Conector a um Agente no Agent Designer

1. No console do Gemini Enterprise, vá até a aba **Agents** (ou **Agent Designer**).
2. Selecione o agente desejado ou crie um novo agente (ex.: `Assistente de Processos & Kanban`).
3. Na seção **Tools & Actions**, clique em **Add Tool / Add Action**.
4. Selecione o conector `Pipefy Operational Hub` criado no passo anterior.
5. Salve e publique a nova versão do Agente.

---

## 4. Exemplos de Interação com o Agente no Gemini Enterprise

Com o conector ativo, o Gemini Enterprise pode executar tarefas operacionais a partir de comandos em linguagem natural:

* **Consulta de Processos:**
  > *"Quais são os pipes ativos na nossa organização do Pipefy e quais são as fases do processo de Helpdesk?"*
* **Triagem de Demandas:**
  > *"Quantos cards estão atualmente na fase 'Aguardando Aprovação' no Pipefy? Liste o título e solicitante de cada um."*
* **Criação de Cards:**
  > *"Crie um novo card no pipe de Compras intitulado 'Aquisição de Licenças de IA' com a justificativa de suporte à equipe de engenharia."*
* **Movimentação de Fases:**
  > *"Mova o card ID 123456 para a fase 'Concluído' e adicione o comentário: 'Aprovado pelo comitê de TI'."*
