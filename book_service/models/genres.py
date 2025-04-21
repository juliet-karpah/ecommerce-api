from sqlmodel import SQLModel, Field

class Genres(SQLModel, table=True):
    id: int = Field(primary_key=True)