from fastapi import FastAPI
from typing import Union

app = FastAPI()

@app.get('/api/hello')
def hello_world():
    return {'hello': 'World'}