from typing import Union
from fastapi import FastAPI
import json

app = FastAPI()


with open('data.json', 'r') as file:
    data = json.load(file)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/books/{book_id}")
def read_item(book_id: int):
    if book_id >= len(data['books']):
        return "Index out of bounds"
    else:
        return data['books'][book_id-1]