
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

book = [book]
    

@app.get("/book/{book_id}")
def get_books(book_id: int):
    for books in book:
        if book_id == book_id:
            return book

    return {"message": "Book not found!"}

@app.post("/books")
def add_book(book: Book):
    books.append(book)
    return book

    raise HTTPexception(
        status_code=404,
        detail="Book not found"
    )