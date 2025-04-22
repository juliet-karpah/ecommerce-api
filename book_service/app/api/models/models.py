from sqlmodel import SQLModel, Field
from typing import Optional
from pydantic import BaseModel  # type: ignore


class Books(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(index=True)
    isbn: Optional[str]
    price: float
    img: str
    description: str
    # genres: list[Genres] = Relationship(back_populates="books", link_model=BookGenresLink)
    # authors: list[Authors] = Relationship(back_populates="books", link_model=BookAuthorLink)
    # stock_quantity: Optional[int]
    # publication_date: Optional[str]


book_1 = Books(
    title="Mansfield Park",
    price=41.14,
    img="https://pictures.abebooks.com/inventory/32151135058.jpg",
    description="Illustrated Edition with unusual transparent dust jacket. The dust jacket has three bits torn out, the largest about 2cm x 2cm, all at the edges (see images). Scholl prize issued 1959 (label inside, see photo). Beautiful Illustrations by Philip Gough. Pages very clean. Beind very strong. ",
)


# engine = create_engine("sqlite:///database.db")


# SQLModel.metadata.create_all(engine)

# with Session(engine) as session:
#     session.add(hero_1)
#     session.add(hero_2)
#     session.add(hero_3)
#     session.commit()

# with Session(engine) as session:
#     statement = select(Hero).where(Hero.name == "Spider-Boy")
#     hero = session.exec(statement).first()
#     print(hero)

# class Genres(SQLModel, table=True):
#     id: int = Field(primary_key=True)

# class BookGenresLink(SQLModel, table=True):
#     book_id: int = Field(foreign_key='books.id', primary_key=True)
#     genre_id: int = Field(foreign_key='genres.id', primary_key=True)

# class BookAuthorLink(SQLModel, table=True):
#     book_id: int = Field(foreign_key="books.id", primary_key=True)
#     author_id: int = Field(foreign_key="authors.id", primary_key=True)


# class Authors(SQLModel, table=True):
#     id: Optional[int] = Field(primary_key=True)
#     name: str
#     website: Optional[str]
#     photo_url: Optional[str]
#     biography: str
#     nationality: str
