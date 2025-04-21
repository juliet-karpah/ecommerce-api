from sqlmodel import Field, SQLModel

class User(SQLModel, table=True):
    id: int = Field(primary_key=True)
    first_name: str
    last_name: str
    email: str
    password: str