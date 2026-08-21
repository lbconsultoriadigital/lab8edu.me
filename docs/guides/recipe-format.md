---
layout: default
title: Padrão de receitas
---

# Padrão de receitas do LBedu

Uma receita LBedu é uma unidade pequena, reproduzível e adaptável de aprendizado. Ela deve resolver um problema claro e permitir que outra pessoa verifique o resultado sem depender de promessas.

## Critérios mínimos

Uma receita aceita precisa:

- resolver um problema específico;
- declarar para quem foi escrita;
- produzir um resultado observável;
- ter passos testados do início ao fim;
- informar requisitos, custos e dependências;
- explicar limitações e riscos;
- não incluir segredos ou dados pessoais;
- indicar autoria e licença de materiais externos.

## Estrutura obrigatória

Copie esta estrutura ao criar uma receita:

```markdown
# Nome orientado ao resultado

## Problema
O que esta receita resolve e em qual contexto.

## Resultado esperado
O que a pessoa verá, produzirá ou conseguirá medir.

## Para quem é
Nível, conhecimentos prévios e casos de uso.

## Tempo estimado
Tempo realista para reproduzir o exemplo.

## Requisitos e custos
Ferramentas, versões, contas, chaves e possíveis cobranças.

## Como usar
Passos completos, comandos copiáveis e arquivos necessários.

## Como verificar
Saída esperada, teste, screenshot ou critério objetivo.

## Compatibilidade
Modelos, provedores, sistemas e versões testadas.

## Limitações e segurança
O que pode falhar, o que não deve ser usado em produção e cuidados necessários.

## Como adaptar
Pontos seguros para personalização e extensões sugeridas.

## Autoria e licença
Autor, contribuidores, fontes e licença de materiais externos.
```

## Selos editoriais

Os selos ajudam a pessoa a decidir antes de executar:

- `Testado`: reproduzido conforme as instruções;
- `Iniciante`: não exige experiência avançada;
- `Sem código`: pode ser usado sem programação;
- `Gratuito`: não exige pagamento no fluxo principal;
- `Requer API`: depende de chave de provedor;
- `Local`: pode funcionar sem enviar conteúdo a um provedor remoto;
- `Experimental`: comportamento ou dependência ainda instável;
- `Community Tested`: validado por pelo menos um contribuidor externo.

Só use um selo quando a condição estiver explícita e verificável na receita.

## Evidência de teste

A evidência pode ser:

- saída esperada no terminal;
- teste automatizado;
- exemplo de entrada e saída sem dados sensíveis;
- captura de tela sem informações privadas;
- comparação documentada entre comportamento esperado e obtido.

Não use apenas “funcionou para mim”. Informe ambiente, versão e limites do teste.

## Nomes e diretórios

- use nomes em minúsculas com hífen: `agente-pesquisa-local`;
- mantenha arquivos necessários próximos da documentação;
- forneça `.env.example`, nunca `.env`;
- prefira exemplos pequenos em vez de frameworks incompletos;
- adicione dependências com versão e arquivo de lock quando aplicável.

## Revisão

A revisão verifica clareza, segurança, reprodutibilidade, licença e aderência ao escopo educacional. Uma receita pode ser aceita como `Experimental` quando a instabilidade estiver claramente documentada.

[Voltar aos guias](index.md) · [Como contribuir](../../CONTRIBUTING.md)
