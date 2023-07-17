FROM ghcr.io/artcode-kazan/python:3.8.12

WORKDIR /service

COPY ${TOML_FILE} .

RUN poetry install 

COPY /project .

ENTRYPOINT ["python3.8", "main.py"]

EXPOSE 3789
