from typing import Union
from fastapi import FastAPI
import json
import books

app = FastAPI()


with open('data.json', 'r') as file:
    books_data = json.load(file)

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/books/{book_id}")
def read_item(book_id: int): #, q: Union[str, None] = None):
    if book_id >= len(books.books):
        return "Index out of bounds"
    else:
        return books.books[book_id-1]
    #return {"book_id": book_id, "q": q}