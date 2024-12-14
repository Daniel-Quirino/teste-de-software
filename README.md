# **Trabalho Prático 1:** Gerenciador de Faturas

[![codecov](https://codecov.io/github/Daniel-Quirino/teste-de-software/graph/badge.svg?token=6EC9M4PCGS)](https://codecov.io/github/Daniel-Quirino/teste-de-software)

**Universidade Federal de Minas Gerais | Departamento de Ciência da Computação | 2024/02**

**Alunos:** Bernardo Reis, Daniel Quirino

**Professor:** André Cavalcante Hora

**Disciplina:** DCC030 Teste de Software

## Introdução

Este projeto teve por objetivo a prática de conceitos e de técnicas associados a **teste de software**. Para isso, foi desenvolvido um sistema simples para controle de faturas. Nele, é possível declarar uma lista de clientes, uma lista de produtos e uma lista de faturas, estas últimas que associam um cliente a um conjunto de produtos no contexto de uma compra. Com isso, é possível se ter controle, por exemplo, das transações que ocorrem em uma loja virtual.

Em um primeiro momento, foram implementados apenas **testes de unidade**, sob pretexto da verificação de unidades pequenas, autocontidas e independentes do código, com destaque para a lógica de negócio. Em etapas futuras, pretende-se implementar **testes de integração e e2e**, completando toda a pirâmide de testes e estabelecendo uma suíte completa para o ecossistema do software implementado, garantindo a sua qualidade ao decorrer do ciclo de desenvolvimento.

## Tecnologias

A implementação do back-end foi feita com a linguagem de programação **Python**. O front-end consiste em uma simples interface via linha de comando, também feita nessa linguagem. A comunicação entre os dois é feita de maneira direta via imports e chamadas de função - eles executam como uma aplicação única e monolítica. Até o momento, não houve a utilização de nenhum serviço externo, como uma **base de dados**. Em termos de **frameworks**, foi utilizado o **pytest** para a escrita, a execução e a geração de relatórios de **coverage** para os testes de unidade. A manipulação dos processos CI/CD que contemplam essa verificação foi feita com base nas pipelines do **GitHub Actions**, com a exportação de resultados para a plataforma **CodeCov**.

Um detalhe importante é que os testes de unidade avaliam apenas os módulos na pasta ```app/services```. O conteúdo do arquivo ```app/main.py```, o qual consiste apenas na implementação da interface de usuário em linha de comando, **não é testado pelos testes de unidade e não é considerado no relatório de cobertura**.

## Instruções de Build e de Execução (Linux)

Na raiz do projeto, primeiramente, deve-se criar um ambiente virtual Python por meio do comando:

```bash
python3 -m venv ./.venv
```

... e o ativar por meio do comando:

```bash
source ./.venv/bin/activate
```

Em seguida, as dependências do sistema devem ser instaladas por meio do comando:

```bash
pip install -r requirements.txt
```

A execução da aplicação pode ser feita por meio do seguinte comando:

```bash
python3 app/main.py
```

Por fim, a execução dos testes com geração de relatório de cobertura pode ser feita por meio do seguinte comando:

```bash
pytest --cov=app tests/
```