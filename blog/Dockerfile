FROM python:3.11-slim

RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python3 - && \
    ln -s /root/.local/bin/poetry /usr/local/bin/poetry && \
    apt-get clean && rm -rf /var/lib/apt/lists/*


WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.create false && poetry install --no-dev --no-interaction --no-ansi

COPY ./start.sh .
RUN sed -i 's/\r$//g' ./start.sh
RUN chmod +x ./start.sh


COPY . .

EXPOSE 8000

ENTRYPOINT ["./start.sh"]