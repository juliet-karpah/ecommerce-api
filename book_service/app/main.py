from fastapi import FastAPI
from app.api.books import books_router

app = FastAPI(
    title="Oldy",
    description="The api for a book store: Oldy But Goodie",
    version="1.0.0",
)

app.include_router(books_router)