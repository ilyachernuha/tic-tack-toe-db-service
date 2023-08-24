from mongoengine import Document, StringField
from pydantic import BaseModel


class User(Document):
    name = StringField(max_length=50)


class UserModel(BaseModel):
    id: str
    name: str


class UserCreate(BaseModel):
    name: str
