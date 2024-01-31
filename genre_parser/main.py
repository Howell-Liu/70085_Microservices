from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import httpx
import os

app = FastAPI()
templates = Jinja2Templates(directory="templates")

BOOK_URL = os.getenv("BOOK_URL")


@app.get('/', response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get('/books', response_class=HTMLResponse)
async def get_book(request: Request, book_id: int = None, genre: str = None):
    if book_id is None and genre is None:
        raise HTTPException(status_code=500, detail="No book id or genre inputted")
    
    if book_id:
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(f"{BOOK_URL}/books/{book_id}")
                response.raise_for_status()  # Raise an exception for HTTP errors
                book_data = response.json()
                return templates.TemplateResponse("book.html", {"request": request, "books": [book_data]})
        except httpx.HTTPStatusError as e:
            # Handle HTTP errors
            raise HTTPException(status_code=e.response.status_code, detail="Book not found")
        except httpx.RequestError:
            # Handle request errors (e.g., network issues)
            raise HTTPException(status_code=500, detail="Internal server error")
        
    if genre:
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(f"{BOOK_URL}/books", params={"genre": genre})
                response.raise_for_status()  # Raise an exception for HTTP errors
                book_data = response.json()
                return templates.TemplateResponse("book.html", {"request": request, "books": book_data})
        except httpx.HTTPStatusError as e:
            raise HTTPException(status_code=e.response.status_code, detail="Book not found")
        except httpx.RequestError:
            raise HTTPException(status_code=500, detail="Internal server error")
