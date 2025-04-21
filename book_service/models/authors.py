from sqlmodel import SQLModel, Field
from typing import Optional

class Authors(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)
    name: str
    website: Optional[str]
    photo_url: Optional[str]
    biography: str
    nationality: str


