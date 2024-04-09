# Blog Post

O Blog Post é uma API rest capaz de armenzar dados de usuários e suas postagens. Foi desenvolvida em Python, utilizando o framework django/django rest.

### Executar Manualmente

Para executar o projeto é necessário ter o python (versão 3.10>=) instalado em seu ambiente. Este projeto utiliza o Poetry para gerenciar dependências. Para instalar o Poetry em seu ambiente, acesse a [documentação](https://python-poetry.org/docs/#installation).

Primeiramente, clone o repositório:

```
git clone https://github.com/hllustosa/blogs-post.git
```

Execute as migrações (este processo irá criar o banco de dados e as tabelas necessárias)

```
make migrate
```

Caso tenha feito alterações nas models, é preciso criar as migrations:

```
make makemigrations
```

Finalmente execute a aplicação:

```
make run
```

### Executar em Docker

O projeto suporta a execução em docker de forma mais conveniente sem a necessidade de instalar dependências extras (além do docker, obviamente). Para executar o projeto via docker utilize os seguintes comandos:

```
git clone https://github.com/hllustosa/blogs-post
cd blogs-post
```

Construa a imagem docker:

```
make build-docker
```

Execute um container com base na imagem criada:
```
make run-docker
```

### Testes e Lint

Os testes da API foram escritos utilizando Pytest. Para testar a API execute o comando:
```
make test
```

Este projeto utiliza a lib pre-commit com diversos plugins para garantir a qualidade do código. Para executar, rode o comando:

```
make lint
```
