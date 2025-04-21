from sqlmodel import SQLModel, Field

class BookAuthorLink(SQLModel, table=True):
    book_id: int = Field(foreign_key="books.id", primary_key=True)
    author_id: int = Field(foreign_key="authors.id", primary_key=True)