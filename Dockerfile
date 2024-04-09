# Stage 1: Imagem base
FROM python:3.10-slim AS base

ENV LANG C.UTF-8
ENV PYTHONUNBUFFERED 1

RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    tzdata \
    git \
    && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    pip install --no-cache-dir poetry==1.2.2 setuptools && poetry config virtualenvs.create false

RUN pip install --upgrade pip && pip install --no-cache-dir gunicorn uvicorn

# Stage 2: Copiando dados do projeto e instalando dependências
FROM base AS setup

WORKDIR /app
COPY pyproject.toml poetry.lock /app/

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV ENV 'PRODUCTION'

EXPOSE 8000
RUN poetry install --no-dev

COPY . /app/

# Stage 3: Executando as migrations do banco
FROM setup AS migrations

RUN poetry run python blogpost/manage.py migrate

# Stage 5: Executando o projeto
FROM migrations AS final
ENTRYPOINT ["gunicorn", "-c", "gunicorn_config.py", "blogpost.wsgi:application"]
