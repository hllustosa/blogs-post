# Blog Post

O Blog Post é uma API rest capaz de armenzar dados de usuários e suas postagens. Foi desenvolvida em Python, utilizando o framework django/DRF e armazena os dados em um SGBD relacional PostgreSQL.

### Executar Manualmente

Para executar o projeto é necessário ter o python (versão 3.8>=) instalado em seu ambiente. É necessário também possuir acesso a um servidor PostgreSQL. Uma vez com essas dependências forem atendidas, execute os seguintes passos: 

Primeiramente, clone o repositório:

``` 
git clone https://github.com/hllustosa/blogs-post.git
```

Edite o arquivo settings.py em <caminho do repositório>/blogpost/blogpost/ de forma a adicionar as credenciais e informações do banco PostgreSQL como abaixo:

    DATABASES = {
		'default': {
			'ENGINE': 'django.db.backends.postgresql_psycopg2',
			'NAME': 'blogpost',
			'USER': 'postgres',
			'PASSWORD': 'postgres',
			'HOST': 'localhost',
			'PORT': '5432'
		}
	}

Edite o host, porta e as credenciais de usuário e senha conforme a sua instalação do PostgreSQL. Após isso, crie manualmente uma base de dados com o nome blogpost (ou outro nome conforme desejar, porém faça o ajuste do campo NAME nas configurações do django).

Após isso, caso queira ter um ambiente virtual com o isolamento das dependências, execute (passo opcional):

```
#Criar ambiente virtual
python3 -m venv ./env

#Ativar ambiente virtual caso esteja utilizando bash no Linux (cada SO tem seu mecanismo de ativação)
source ./env/bin/activate
```

Instale as dependências do projeto
```
pip3 install -r requirements.txt
```

Execute as migrações (este processo irá criar o banco de dados e as tabelas necessárias)

```
python3 blogpost/manage.py makemigrations
python3 blogpost/manage.py migrate
```

Finalmente execute a aplicação:

```
python3 blogpost/manage.py runserver 0.0.0.0:8000
```

### Executar em Docker

O projeto suporta a execução em docker de forma mais conveniente sem a necessidade de instalar dependências extras (além do docker, obviamente). Para executar o projeto via docker utilize os seguintes comandos:

```
git clone https://github.com/hllustosa/blogs-post
cd blogs-post
docker-compose up -d
``` 

### Testando a API

Após a execução, a aplicação estará disponível a partir desse momento em http://localhost:8000
Este [collection do postman](www.google.com) contém um conjunto de testes e documentação completa da API e de todos os métodos.


