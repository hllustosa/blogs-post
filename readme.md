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

### Testando a API

Após a execução, a aplicação estará disponível a partir desse momento em http://localhost:8000
Esta [collection do postman](https://github.com/hllustosa/blogs-post/blob/master/tests/Blog%20Post.postman_collection.json) contém um conjunto de testes e documentação completa da API e de todos os métodos.


### Mais informações

[Este vídeo](https://youtu.be/Kkz8FLLPztA) contém uma demonstração da API em execução.

Para mais projetos meus, acesse:

- [Aplicação Para Execução de Exercícios de Programação em Python (Python/Microsserviços)](https://github.com/hllustosa/online-judge)

- [Aplicação de Censo em Microsserviços (.Net e ReactJS)](https://github.com/hllustosa/censo-demografico)

- [Aplicação para registro de empréstimos de jogos em (.Net e ReactJS)](https://github.com/hllustosa/game-manager)
