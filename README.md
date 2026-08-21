# LBedu

> Receitas open source de IA que você copia, testa e adapta.

[![Quality checks](https://github.com/lbconsultoriadigital/lbedu.me/actions/workflows/quality.yml/badge.svg)](https://github.com/lbconsultoriadigital/lbedu.me/actions/workflows/quality.yml)
[![License: MIT](https://img.shields.io/badge/licen%C3%A7a-MIT-yellow.svg)](LICENSE)
[![PRs welcome](https://img.shields.io/badge/PRs-bem--vindos-brightgreen.svg)](CONTRIBUTING.md)

O **LBedu** é um projeto educacional, não comercial e aberto para quem quer transformar IA em algo reproduzível. Aqui, prompts, agentes, automações e integrações são publicados com instruções claras, limitações explícitas e caminhos para adaptação.

[Site](https://lbedu.me) · [Guias](docs/guides/index.md) · [Contribua](CONTRIBUTING.md) · [Roadmap](ROADMAP.md)

## Comece por uma receita

| Receita | O que você aprende | Tempo | Requisitos |
| --- | --- | ---: | --- |
| [Prompt de Engenheiro de Software](prompts/software-engineer.md) | Estruturar respostas com arquitetura, segurança e testes | 5 min | Um assistente de IA |
| [Agente mínimo em Python](templates/python-agent-boilerplate/README.md) | Registrar ferramentas e executar entradas com segurança | 10 min | Python 3.10+ |
| [Claude com streaming em Node.js](templates/node-claude-quickstart/README.md) | Consumir a API oficial com respostas em streaming | 10 min | Node.js 18+ e chave da Anthropic |

Quer entender o projeto antes de executar algo? Consulte o [guia de início rápido](docs/guides/getting-started.md).

## O que torna uma receita LBedu

Cada receita deve apresentar:

1. problema específico;
2. resultado esperado;
3. forma de testar ou demonstração;
4. instruções de uso em poucos minutos;
5. requisitos, custos e compatibilidade;
6. limitações, riscos e cuidados de segurança;
7. caminhos para adaptação;
8. autoria e contribuições.

Veja o [padrão completo de receitas](docs/guides/recipe-format.md).

## Inventário atual

- [`prompts/`](prompts/README.md): dois prompts de sistema bilíngues para engenharia de software e arquitetura de agentes.
- [`templates/`](templates/README.md): um exemplo seguro em Python e um quickstart da API Claude em Node.js.
- [`mcp-servers/`](mcp-servers/README.md): material introdutório bilíngue sobre Model Context Protocol; implementações executáveis estão no roadmap.
- [`docs/guides/`](docs/guides/index.md): guias de início e padrões editoriais.

O README descreve somente recursos que existem no repositório. Novas integrações entram depois de implementadas, testadas e documentadas.

## Execute localmente

```bash
git clone https://github.com/lbconsultoriadigital/lbedu.me.git
cd lbedu.me
```

### Exemplo Python

```bash
cd templates/python-agent-boilerplate
python main.py
python -m unittest
```

### Exemplo Node.js

```bash
cd templates/node-claude-quickstart
npm ci
cp .env.example .env
npm start
```

O exemplo Node.js requer uma chave válida da Anthropic. Nunca publique arquivos `.env` ou credenciais.

## Contribua em 10 minutos

Você não precisa começar com código. É possível:

- relatar um problema;
- melhorar uma explicação;
- testar uma receita e registrar o resultado;
- sugerir uma adaptação;
- propor uma nova receita pelo formulário de issue.

Leia o [guia de contribuição](CONTRIBUTING.md), escolha um item marcado como `good first issue` ou use um dos formulários em [Issues](https://github.com/lbconsultoriadigital/lbedu.me/issues/new/choose).

## Qualidade e transparência

- links internos são validados automaticamente;
- os exemplos Python e Node.js passam por verificações no GitHub Actions;
- custos, dependências e limitações devem ser declarados;
- exemplos educacionais não são apresentados como soluções prontas para produção;
- contribuições podem receber crédito no histórico, na receita correspondente e nas notas de release, quando aplicável.

Consulte também [Segurança](SECURITY.md), [Suporte](SUPPORT.md), [Código de Conduta](CODE_OF_CONDUCT.md) e [Changelog](CHANGELOG.md).

## English summary

**LBedu** is a Portuguese-first, noncommercial open-source project for practical AI recipes you can copy, test, and adapt. Every accepted resource should include a reproducible outcome, setup instructions, requirements, limitations, safety notes, and contributor credit. Start with the recipes above or read the [contribution guide](CONTRIBUTING.md).

## Licença

Distribuído sob a [licença MIT](LICENSE).
