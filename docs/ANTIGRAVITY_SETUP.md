# Integrando o Pipefy MCP ao Google Antigravity (100% Gratuito)

Este guia ensina como plugar o servidor Pipefy MCP diretamente no **Google Antigravity** para desenvolvimento diário, testes locais e demonstração de portfólio sem nenhum custo de infraestrutura.

---

## 1. Modos de Conexão no Antigravity

Você pode conectar o Antigravity ao servidor Pipefy de duas maneiras:

| Modo | Transporte | Vantagens | Recomendado para |
| :--- | :--- | :--- | :--- |
| **Modo 1: STDIO Local** | Processo stdio | Zero portas de rede abertas; máxima performance local; inicia sob demanda. | Desenvolvimento local rápido e seguro. |
| **Modo 2: HTTP Local** | StreamableHTTP (`http://localhost:8080/mcp`) | Simula exatamente o mesmo ambiente que o Cloud Run usará para o Gemini Enterprise. | Homologação pré-deploy do Gemini Enterprise. |

---

## 2. Configurando o Antigravity

### Opção 1: Configuração via STDIO (Recomendada para uso local)
Adicione o servidor na configuração de servidores MCP do Antigravity (ou Claude Desktop / Cursor):

```json
{
  "mcpServers": {
    "pipefy": {
      "command": "python",
      "args": ["-m", "src.run_server", "--stdio"],
      "cwd": "C:/Users/STR69/Documents/mcp pipefy",
      "env": {
        "PIPEFY_TOKEN": "SEU_PERSONAL_TOKEN_AQUI",
        "PIPEFY_MCP_TOOLSETS": "cards,pipes,tables"
      }
    }
  }
}
```

*Dica:* Se você utiliza `uv`, pode substituir o `command` por `uv` e `args` por `["run", "python", "-m", "src.run_server", "--stdio"]`.

### Opção 2: Conexão via StreamableHTTP Local
1. Em um terminal, inicie o servidor local:
   ```bash
   python -m src.run_server
   ```
   *(O servidor iniciará em `http://0.0.0.0:8080/mcp` com `StreamableHTTP` ativo).*
2. Configure o Antigravity para se conectar via URL HTTP:
   ```json
   {
     "mcpServers": {
       "pipefy": {
         "url": "http://localhost:8080/mcp"
       }
     }
   }
   ```

---

## 3. Testando as Ferramentas no Antigravity

Com o servidor registrado, você pode conversar com o Antigravity usando comandos como:

* *"Liste meus pipes do Pipefy e verifique quantos cards existem em cada fase."*
* *"Busque detalhes do card de ID 123456 no Pipefy."*
* *"Crie um card de bug no pipe de TI com prioridade alta."*
* *"Adicione uma nota no card informando que a correção foi enviada para homologação."*

O Antigravity identificará as ferramentas do Pipefy via MCP e executará as chamadas de API automaticamente.
