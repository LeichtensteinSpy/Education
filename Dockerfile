FROM ghcr.io/artcode-kazan/python:3.8.12

WORKDIR /service

COPY .pyproject.toml .

RUN poetry install 

COPY ./project .

ENTRYPOINT ["python3.8", "main.py"]

EXPOSE 3789
