from sqlmodel import SQLModel, Field

class BookGenresLink(SQLModel, table=True):
    book_id: int = Field(foreign_key='books.id', primary_key=True)
    genre_id: int = Field(foreign_key='genres.id', primary_key=True)