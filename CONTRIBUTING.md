# Como contribuir com o LBedu

Obrigado por ajudar a construir uma biblioteca aberta de IA prática em português. Contribuições de documentação, testes, exemplos, acessibilidade e código são bem-vindas.

Ao participar, você concorda com o [Código de Conduta](CODE_OF_CONDUCT.md). Problemas de segurança devem seguir a [Política de Segurança](SECURITY.md), nunca uma issue pública.

## Contribua em 10 minutos

A forma mais simples de começar é usar os formulários em [Nova issue](https://github.com/lbconsultoriadigital/lbedu.me/issues/new/choose):

1. relate um erro reproduzível;
2. sugira uma melhoria de documentação;
3. proponha uma receita com problema e resultado claros;
4. teste um exemplo existente e compartilhe o resultado;
5. escolha uma issue marcada como `good first issue`.

Não é necessário pedir permissão antes de corrigir um erro pequeno. Para mudanças grandes, abra uma proposta antes de investir tempo na implementação.

## O que aceitamos

- prompts estruturados e testáveis;
- pequenos agentes e automações educacionais;
- templates executáveis com instruções de verificação;
- exemplos e guias de Model Context Protocol;
- correções de bugs, segurança, acessibilidade e documentação;
- traduções que preservem o conteúdo em português como versão principal.

Listas de links sem curadoria, material vazado, credenciais, conteúdo copiado sem licença e promessas sem demonstração não serão aceitos.

## Padrão de receita

Novas receitas devem seguir o [formato oficial](docs/guides/recipe-format.md). Em resumo, inclua:

- problema e público;
- resultado esperado;
- instruções reproduzíveis;
- requisitos e custos;
- compatibilidade;
- limitações e segurança;
- evidência do teste;
- autoria e licença de materiais externos.

## Fluxo de trabalho

1. Faça um fork e clone o repositório:

   ```bash
   git clone https://github.com/SEU-USUARIO/lbedu.me.git
   cd lbedu.me
   ```

2. Crie uma branch curta e descritiva:

   ```bash
   git switch -c feat/nome-da-receita
   # ou
   git switch -c docs/melhoria-do-guia
   # ou
   git switch -c fix/descricao-do-problema
   ```

3. Faça uma mudança focada. Evite misturar refatoração, conteúdo e correção de bug no mesmo PR.

4. Execute as verificações aplicáveis:

   ```bash
   python .github/scripts/check_internal_links.py
   (cd templates/python-agent-boilerplate && python -m unittest && python main.py)
   (cd templates/node-claude-quickstart && npm ci --ignore-scripts --no-audit --no-fund && node --check index.mjs)
   ```

5. Use Conventional Commits:

   - `feat:` nova receita, template ou funcionalidade;
   - `fix:` correção de comportamento;
   - `docs:` documentação;
   - `test:` testes;
   - `chore:` manutenção.

6. Abra um Pull Request e preencha o checklist. Explique o resultado, como foi testado e quais limitações permanecem.

## Checklist antes do PR

- [ ] O conteúdo resolve um problema específico.
- [ ] Os passos foram executados do início ao fim.
- [ ] Não há chaves, tokens, dados pessoais ou arquivos `.env` versionados.
- [ ] Custos e dependências externas estão claros.
- [ ] Limitações e riscos estão documentados.
- [ ] Links internos passam no validador.
- [ ] Materiais externos têm fonte e licença compatíveis.
- [ ] A documentação em português está completa.

## Revisão e reconhecimento

A manutenção pode solicitar mudanças para tornar o exemplo mais seguro, simples ou reproduzível. O objetivo da revisão é melhorar o conteúdo, não avaliar a pessoa.

Contribuidores aprovados podem receber crédito no histórico do Git, na receita correspondente e nas notas de release, quando aplicável. Destaques comunitários e publicações colaborativas podem ser usados com autorização do autor.

## Precisa de ajuda?

Consulte [SUPPORT.md](SUPPORT.md) para escolher o canal adequado. Dúvidas públicas e reproduzíveis ajudam outras pessoas; informações privadas nunca devem ser publicadas em issues.
