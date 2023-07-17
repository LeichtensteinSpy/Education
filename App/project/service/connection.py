"""Module with psycopg2 connection."""

import os

import psycopg2
from dotenv import load_dotenv

load_dotenv()


def create_connection():
    connection = psycopg2.connect(
        dbname=os.getenv('POSTGRES_DB'),
        user=os.getenv('POSTGRES_USER'),
        password=os.getenv('POSTGRES_PASSWORD'),
        host=os.getenv('POSTGRES_HOST'),
        port=os.getenv('POSTGRES_PORT')
    )
    return connection
