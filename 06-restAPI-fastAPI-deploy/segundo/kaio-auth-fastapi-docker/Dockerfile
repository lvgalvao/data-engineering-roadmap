FROM python:3.12 as builder

ENV PIP_YES=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

WORKDIR /app

COPY pyproject.toml poetry.lock /app/
RUN touch README.md

RUN --mount=type=cache,target=$POETRY_CACHE_DIR \
    pip install poetry==1.8.2 && \
    poetry install --only main --no-root

FROM python:3.12-slim as runtime

ENV VIRTUAL_ENV=/app/.venv \
    PATH="/app/.venv/bin:$PATH"

WORKDIR /app

COPY --from=builder $VIRTUAL_ENV $VIRTUAL_ENV
COPY src ./src
EXPOSE 8000
#ENTRYPOINT [ "gunicorn", "src.main:app", "--workers", "4", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8000" ]
ENTRYPOINT [ "uvicorn", "src.main:app", "--host", "127.0.0.1", "--port", "8000" ]
