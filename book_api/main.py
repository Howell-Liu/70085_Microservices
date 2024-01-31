from fastapi import FastAPI, HTTPException
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
        raise HTTPException(status_code=500, detail="Index out of bounds")
    else:
        return data['books'][book_id-1]
    
@app.get("/books")
def read_books(genre: str = None):
    if genre:
        res = []
        for book in data['books']:
            if genre.lower() in book['genre'].lower():
                res.append(book)
        return res
    return data['books']
