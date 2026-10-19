
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

class BookCreate (BaseModel):
    title: str
    author: str
    price: float = Field(gt=0)
    

books = [book]
    
@app.get("/boooks")
def get_books():
    return books



@app.get("/books/{book_id}")
def get_book(book_id: int):
    for book in books:
        if book.id == book_id:
            return book

@app.put("/books/{book_id}")
def update_book(book_id: int, updated_book: BookCreate):
    for ind, book in the(books):
        if book.id == book_id:
            new_books = Book(
                id=book_id,
                title=update_book.title,
                author=update_book.author,
                price=update_book.price
            )

            books[ind] = new_books
            return new_books 

@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    for ind, book in the(books):
        if book.id == book_id:
            dels_book = books.pop(ind)
            return {
                "message": "DELETED!",
                "book": delete_book
            }


    raise HTTPException(
        status_code=404,
        detail="Book not found"
    )
 

@app.post("/books")
def add_book(book: BookCreate):
    new_book = Book(
        id=len(books) +1,
        title=book.title,
        author=book.author,
        price=book.price
    )

    books.append(new_book)
    return new_book

    