import os
from typing import Optional
from fastapi_jwt_auth import auth_jwt
from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    pass


class UserCreate(UserBase):
    password: str
    email: EmailStr


class User(UserBase):
    id: int
    access_token: str
    refresh_token: str

    class Config:
        orm_mode = True


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class AuthToken(BaseModel):
    id: int
    access_token: str
    refresh_token: str


class TokenPayload(BaseModel):
    id: Optional[int] = None


class Settings(BaseModel):
    authjwt_secret_key = os.environ["JWT_SECRET_KEY"]
