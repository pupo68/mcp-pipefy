# Product Guidelines

## 1. Princípios de Arquitetura e Engenharia
* **Padronização MCP First:** Aderência estrita à especificação aberta do Model Context Protocol (MCP 2.0 / StreamableHTTP), garantindo interoperabilidade com qualquer cliente MCP (Gemini, Antigravity, Claude, Cursor).
* **Cloud-Native & Custo Zero (Free Tier):** Priorização de infraestrutura sem custos de manutenção (Google Cloud Run scale-to-zero, Docker slim, consumo sob demanda).
* **Segurança e Privilégio Mínimo:**
  * Proibição absoluta de credenciais ou tokens em código versionado.
  * Suporte a injeção segura de credenciais via variáveis de ambiente (`.env`) ou Google Secret Manager.
  * Validação prévia de tokens na inicialização do serviço.

## 2. Princípios de Experiência do Agente de IA (Tool UX)
* **Descrições Ricas e Determinísticas:** Ferramentas MCP devem possuir descrições claras de parâmetros e retornos para minimizar alucinações e erros de invocação dos modelos Gemini e Antigravity.
* **Curadoria e Foco:** Manter o conjunto de ações ativo enxuto e de alto valor (abaixo de 100 ações), priorizando tarefas de alto impacto operacional.
* **Mensagens de Erro Acionáveis:** Se uma requisição falhar (ex.: campo obrigatório ausente ou permissão insuficiente no Pipefy), a resposta deve orientar a IA com clareza sobre o que ajustar.

## 3. Padrões de Portfólio e Documentação
* **Código Limpo e Autoexplicativo:** Python moderno (type hints completos, async/await, estrutura modular).
* **Guia de Setup Reproduzível:** Documentação clara e concisa no repositório permitindo que qualquer avaliador ou desenvolvedor clone e execute o servidor em menos de 5 minutos (localmente ou no Cloud Run).
