FROM ghcr.io/artcode-kazan/python:3.8.12

RUN apt-get -y update

WORKDIR /service

COPY ./pyproject.toml .

RUN poetry install --only main

COPY ./project .

ENTRYPOINT ["python3.8", "main.py"]

EXPOSE 3789