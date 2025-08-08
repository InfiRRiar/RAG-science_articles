FROM python:3.10-slim

WORKDIR /app
COPY web/app.py /app/

ENV POETRY_VIRTUALENVS_CREATE=false

RUN pip install poetry
COPY poetry.lock pyproject.toml /app/

EXPOSE 8000

RUN poetry install --with web --no-root

CMD ["fastapi", "run", "app.py"]