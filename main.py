
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="Bookstore API")

@app.get("/")
def home():
    return {"message": "Welcome to the Bookstore API"}

class Book(BaseModel):
    id: int
    title: str
    author: str
    price: float = Field(gt=0)

book = Book (
    id=1,
    title="Basic Python",
    author="Lian Angelo Cruspero",
    price=350
)

books = [book]
    

@app.get("/books/{book_id}")
def get_book(book_id: int):
    for book in books:
        if book.id == book_id:
            return book

    raise HTTPException(
        status_code=404,
        detail="Book not found"
    )

@app.post("/books")
def add_book(book: Book):
    books.append(book)
    return book

    