from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from genres import Genres
from book_service.models.authors import Authors
from book_service.book_authors import BookAuthorLink
from book_service.book_genres import BookGenresLink

class Books(SQLModel, table=True):
    id: int = Field(primary=True)
    title: str
    isbn: str
    price: float
    img: str
    description: str
    genres: list[Genres] = Relationship(back_populates="books", link_model=BookGenresLink)
    authors: list[Authors] = Relationship(back_populates="books", link_model=BookAuthorLink)
    stock_quantity: int
    publication_date: str

    