from fastapi import FastAPI
import json

app = FastAPI()

with open('data.json', 'r') as file:
    books_data = json.load(file)

@app.get("/")
async def root():
    return books_data