FROM python:3.10-slim-buster

WORKDIR /app

COPY . .

RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --only main --no-interaction --no-ansi --no-root

CMD [ "python", "main.py" ]
