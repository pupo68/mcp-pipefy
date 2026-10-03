# Python Code Style Guide

## 1. Formatação e Sintaxe
* **Indetação:** 4 espaços (nunca tabs).
* **Comprimento de Linha:** Limite de 100 caracteres.
* **Imports:**
  1. Biblioteca padrão do Python (`os`, `sys`, `typing`, `logging`, etc.).
  2. Bibliotecas de terceiros (`mcp`, `httpx`, `pydantic`, `starlette`, etc.).
  3. Módulos locais do projeto.
  * Sempre ordenados alfabeticamente dentro de cada bloco.

## 2. Tipagem Estática (Type Hints)
* Todos os argumentos de função e valores de retorno devem possuir anotações de tipo explícitas (`from __future__ import annotations`, `str | None`, `Sequence[str]`, etc.).
* Modelos de dados de entrada e saída devem utilizar **Pydantic v2** (`BaseModel`, `Field`).

## 3. Concorrência e Assincronismo
* Funções de I/O de rede (como chamadas à API GraphQL do Pipefy) devem ser estritamente assíncronas (`async def`, `await client.post(...)`).
* Utilizar `httpx.AsyncClient` com context manager ou ciclo de vida gerenciado (`lifespan`).

## 4. Tratamento de Erros e Logs
* Usar o módulo `logging` estruturado em vez de `print`.
* Capturar exceções específicas (ex.: `httpx.HTTPStatusError`, `httpx.RequestError`) e retornar mensagens de erro ricas e amigáveis ao modelo de IA.
* Nunca mascarar erros silenciosamente sem logar o contexto.

## 5. Convenções MCP
* Cada tool MCP registrada com `@mcp.tool()` deve conter uma docstring rica e detalhada explicando o objetivo da ferramenta, cada argumento e o formato da resposta.
