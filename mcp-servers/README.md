# Model Context Protocol (MCP) Hub

[Português](#português) | [English](#english)

---

<a name="português"></a>
## Português

O **Model Context Protocol (MCP)** é um padrão aberto desenvolvido pela Anthropic que permite a comunicação segura e bidirecional entre aplicações de IA (como Claude Desktop e Agentes de IA) e fontes de dados locais ou remotas, ferramentas de desenvolvedor e APIs.

### Conceitos Fundamentais

- **Aplicação Hospedeira (Host)**: O cliente de IA que faz as solicitações (ex: Claude Desktop, Aside, agentes customizados).
- **Servidor MCP**: Um processo leve que expõe ferramentas, recursos e modelos de prompts específicos.
- **Transportes do Protocolo**: Entrada/saída padrão (`stdio`) para ferramentas locais ou Server-Sent Events (`SSE`) para integrações em rede.

### Próximos módulos deste diretório:
- [x] Especificações e visão geral de arquitetura.
- [ ] Template de servidor MCP customizado em TypeScript/Node.js.
- [ ] Template de servidor MCP com FastMCP em Python.

---

<a name="english"></a>
## English

The **Model Context Protocol (MCP)** is an open standard developed by Anthropic that enables secure, bi-directional communication between LLM applications (such as Claude Desktop and AI Agents) and local or remote data sources, developer tools, and APIs.

### Key Concepts

- **Host Application**: The AI client initiating requests (e.g. Claude Desktop, Aside, custom agents).
- **MCP Server**: A lightweight process exposing specific tools, resources, and prompt templates.
- **Protocol Transports**: Standard input/output (`stdio`) for local processes or Server-Sent Events (`SSE`) for network-based tools.

### Roadmap for this directory:
- [x] Protocol specifications and conceptual overview.
- [ ] TypeScript/Node.js custom MCP server template.
- [ ] Python FastMCP server template.
