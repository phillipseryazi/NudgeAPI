from datetime import datetime
from typing import Dict, List, Optional
from pydantic import BaseModel, EmailStr
from sqlalchemy.sql.sqltypes import TIMESTAMP


class BusinessBase(BaseModel):
    pass


class BusinessCreate(BusinessBase):
    user_id: Optional[int]
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
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
