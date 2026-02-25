from pydantic import BaseModel
from datetime import date


class UserBase(BaseModel):
    login: str
    password: str


class User(UserBase):
    id: int


class UserCreate(UserBase):
    pass


class MessageBase(BaseModel):
    Data: date
    Name: str
    place: str
    tel_num: str
    email: str
    factory_numbers: str
    device_type: str
    emotional: str
    main: str


class MessageCreate(MessageBase):
    pass


class Message(MessageBase):
    id: int
