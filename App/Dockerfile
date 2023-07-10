FROM debian:bullseye-slim

WORKDIR /App

COPY . .

RUN apt-get -y update && apt-get -y install python3-pip && apt-get -y install python3

RUN pip3 install poetry && poetry update

RUN poetry install --only main

RUN pip3 install uvicorn && pip3 install fastapi

CMD ["python3", "project/main.py"]

EXPOSE 3789