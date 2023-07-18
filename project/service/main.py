"""Main module."""

import os

import uvicorn
from fastapi import FastAPI
from service.connection import create_connection

app = FastAPI()


@app.get('/get')
async def get() -> dict:
    """Return message.

    Returns: dict with message

    """
    return {'message': 'Wake up, Tim!'}


@app.post('/post')
async def post(name: str) -> dict:
    """Return message with request status.

    Args:
        name: name

    Return: dict with message status
    """
    query = 'INSERT INTO samples (name) VALUES (%s)'
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute(query, (name,))
    connection.commit()
    cursor.close()
    return {'message': 'All good'}


@app.get('/get-all')
async def get_all() -> dict:
    """Return dict with records list.

    Return: dict with records list
    """
    query = "SELECT * FROM samples"
    cursor = create_connection().cursor()
    cursor.execute(query)
    returning_records = []
    records = cursor.fetchall()
    for record in records:
        returning_records.append(record)
    return {'data': returning_records}


if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        reload=True,
        host=os.getenv('APP_HOST'),
        port=int(os.getenv('APP_PORT'))
    )
