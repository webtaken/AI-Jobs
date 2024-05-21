FROM python:3.11-slim-buster as base

# Crear un usuario no root para ejecutar nuestra aplicación
# RUN useradd -m marcacionesnoc
ARG RAILWAY_SERVICE_ID

RUN apt-get update \
  && apt-get -y install libpq-dev gcc python-psycopg2 \
  && apt-get clean

# --- Build Stage ---
FROM python:3.11-buster as builder

RUN echo $RAILWAY_SERVICE_ID

RUN --mount=type=cache,id=s/$RAILWAY_SERVICE_ID-/root/.cache/pip,target=/root/.cache/pip \
  pip install poetry==1.4.2

ENV POETRY_NO_INTERACTION=1 \
  POETRY_VIRTUALENVS_IN_PROJECT=1 \
  POETRY_VIRTUALENVS_CREATE=1 \
  POETRY_CACHE_DIR=/tmp/poetry_cache

WORKDIR /app

COPY pyproject.toml poetry.lock ./
RUN touch README.md

RUN poetry install --only main --no-root && rm -rf $POETRY_CACHE_DIR
RUN poetry add gunicorn

# --- Final Stage ---
FROM base as final

WORKDIR /app
ENV VIRTUAL_ENV=/app/.venv \
  PATH="/app/.venv/bin:$PATH" \
  RAILWAY_DOCKERFILE_PATH=/back

# Copiar el artefacto de build y las dependencias instaladas desde el stage anterior
COPY ./ ./
COPY --from=builder ${VIRTUAL_ENV} ${VIRTUAL_ENV}

# Configurar Whitenoise para servir archivos estáticos
ENV DJANGO_SETTINGS_MODULE=config.settings.prod

COPY --chown=django:django ./start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

# RUN python manage.py collectstatic --noinput

# USER marcacionesnoc

# Establecer el puerto en el que se ejecutará la aplicación
EXPOSE 8000

# Comando para ejecutar la aplicación
# CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]
CMD ["/start"]