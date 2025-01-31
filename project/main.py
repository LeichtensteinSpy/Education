"""Main module."""

import uvicorn

from fastapi import FastAPI

app = FastAPI()


@app.get('/get')
async def get() -> dict:
"""Return message.

Returns: dict with message

"""
    return {'message': 'Wake up, Tim!'}


if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        reload=True,
        host='0.0.0.0',
        port=3789
    )
    
