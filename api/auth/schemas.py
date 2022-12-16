from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class UserCreate(BaseModel):
    email: str = Field(..., example="taysir.boubaker2082@gmail.com")
    password: str = Field(..., example="tayb")
    fullname: str = Field(..., example="Tayssir Boubaker")
    status: str = '0'


class UserList(BaseModel):
    id: int = None
    email: str
    fullname: str
    created_on: Optional[datetime] = None
    status: str = None


class UserListStatus(UserList):
    status: str


class UserPWD(UserList):
    password: str


class UserBasicInfo(BaseModel):
    id: str
    email: str
    fullname: str


class Token(BaseModel):
    access_token: str
    token_type: str
    user_info: UserBasicInfo


class TokenData(BaseModel):
    email: str = None

