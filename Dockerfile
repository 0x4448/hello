FROM python:3.9.5-alpine3.13 AS base

ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Builder stage generates requirements.txt from pyproject.toml
FROM base AS builder

ENV PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 \
    POETRY_VERSION=1.1.6

# Poetry depends on cryptography
# Packages required to build cryptography
RUN apk add --no-cache \
    cargo \
    gcc \
    libffi-dev \
    libressl-dev \
    musl-dev
RUN pip install "poetry==$POETRY_VERSION"

COPY pyproject.toml poetry.lock ./
RUN poetry export -f requirements.txt > /requirements.txt


FROM base AS final

COPY --from=builder /requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY hello/ .
ENTRYPOINT [ "/app/docker-entrypoint.sh" ]