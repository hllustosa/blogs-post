lint:
	poetry run pre-commit install && poetry run pre-commit run -a -v

test:
	poetry run pytest -sx

run:
	poetry run python blogpost/manage.py runserver 0.0.0.0:8000

makemigrations:
	poetry run python blogpost/manage.py makemigrations

migrate:
	poetry run python blogpost/manage.py migrate

build-docker:
	docker build -t blogpost .

run-docker:
	docker run -p 8000:8000 blogpost
