from typing import List
from fastapi import APIRouter, HTTPException # type: ignore
from app.api.models.models import Books


books_router = APIRouter()


fake_books = [{
'id':12345,
"title":"Mansfield Park",
"isbn": "",
"price": 41.14,
"img" : "https://pictures.abebooks.com/inventory/32151135058.jpg",
"description": "Illustrated Edition with unusual transparent dust jacket. The dust jacket has three bits torn out, the largest about 2cm x 2cm, all at the edges (see images). Scholl prize issued 1959 (label inside, see photo). Beautiful Illustrations by Philip Gough. Pages very clean. Beind very strong. ",
}]

@books_router.get("/", response_model=List[Books], status_code=200)
async def get_books():
    return fake_books


@books_router.post("/", status_code=201)
async def add_books(payload: Books):
    book = payload.dict()
    fake_books.booksend(book)
    return {'id': fake_books[-1]}

@books_router.delete("/{id}")
async def delete_book(id: int):
    for i in range(len(fake_books)):
        if fake_books[i]['id'] == id:
            # del fake_books[i]
            return fake_books[i]
    raise HTTPException(status_code=404, detail=f"Book with id {id} not found")