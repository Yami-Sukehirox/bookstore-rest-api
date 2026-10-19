from database import get_connection
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
    
@app.get("/books")
def get_books():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()

    cursor.close()
    connection.close()

    return books



@app.get("/books/{book_id}")
def get_book(book_id: int):
    for book in books:
        if book.id == book_id:
            return book

@app.put("/books/{book_id}")
def update_book(book_id: int, updated_book: BookCreate):
    for ind, book in enumerate(books):
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
    connection = get_connection()
    cursor = connection.cursor()

    try:
        cursor.execute(
            "DELETE FROM books WHERE id = %s",
            (book_id,)
        )

        if cursor.rowcount == 0:
            connection.rollback()
            raise HTTPException(
                status_code=404,
                detail="Book not found in database"
            )

        connection.commit()

        return {
            "message": "Book deleted successfully",
            "book_id": book_id
        }

    finally:
        cursor.close()
        connection.close()


@app.post("/books")
def add_book(book: BookCreate):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO books (title, author, price) VALUES (%s, %s, %s)",
        (book.title, book.author, book.price)
    )

    connection.commit()

    new_book_id = cursor.lastrowid

    cursor.close()
    connection.close()

    return {
        "id": new_book_id,
        "title": book.title,
        "author": book.author,
        "price": book.price
    }

    