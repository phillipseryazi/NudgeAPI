from typing import Dict, List
from pydantic import BaseModel, EmailStr
from sqlalchemy.sql.sqltypes import TIMESTAMP


class BusinessBase(BaseModel):
    pass


class BusinessCreate(BusinessBase):
    name: str
    description: str
    domain: List[str]
    contacts: List[str]
    email: EmailStr


class Business(BusinessBase):
    id: int
    user_id: int
    name: str
    description: str
    domain: List[str]
    contacts: List[str]
    email: EmailStr
    created_at: TIMESTAMP
    updated_at: TIMESTAMP

    class Config:
        orm_mode = True
