
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="Bookstore API")

class book(BaseModel):
    Title: str
    Author: str
    Price: float = Field(gt=0)

book = {
    "title": "Basic Python",
    "author": "Lian Cruspero",
    "pice": 350
}

@app.get("/")
def home():
    return book