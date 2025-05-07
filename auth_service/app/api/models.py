from pydantic import BaseModel
from datetime import datetime

class UserBase(BaseModel):
    first_name: str
    last_name: str
    email: str

class UserSignUp(UserBase):
    password: str

class User(UserBase):
    id: int
    date_created: datetime

class UserSignin(BaseModel):
    email: str
    password: str