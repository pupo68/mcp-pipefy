# Development Workflow

## 1. Princípios de Execução
* **Ciclos Incrementais (Tracks):** Cada funcionalidade, integração ou correção é tratada como uma Track independente com `spec.md`, `plan.md` e `metadata.json`.
* **Test-Driven & Verification-First (TDD):**
  1. Definir contratos de interfaces e testes (unitários/mocks ou integração).
  2. Implementar a lógica mínima para passar nos testes.
  3. Refatorar mantendo cobertura e conformidade de estilo.
* **Surgical Edits Only:** Modificações de código pontuais preservando comentários, formatação e contexto original.

## 2. Fases de uma Track
1. **Fase 1: Especificação e Setup**
   - Criação da especificação detalhada de requisitos e schema de ferramentas.
2. **Fase 2: Implementação e Testes Automatizados**
   - Criação do cliente e registro de tools MCP.
   - Testes de transporte e validação de parâmetros.
3. **Fase 3: Verificação e Checkpointing**
   - Validação ponta a ponta (E2E) com simuladores de cliente MCP e verificação manual pelo usuário.
   - Meta-tarefa obrigatória ao final de cada fase:
     `- [ ] Task: Conductor - User Manual Verification '<Phase Name>' (Protocol in workflow.md)`

## 3. Gestão de Commits e Versionamento
* Mensagens semânticas padronizadas (ex.: `feat(mcp): ...`, `fix(auth): ...`, `chore(deploy): ...`).
* Commits atômicos ao final de cada sub-tarefa validada.
