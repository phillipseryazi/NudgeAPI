from sqlalchemy.sql.expression import null, text
from sqlalchemy.sql.sqltypes import TIMESTAMP, Integer, String
from storage.database import Base
from sqlalchemy import Column


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))


class Blacklist(Base):
    __tablename__ = "tokens"
    id = Column(Integer, primary_key=True, nullable=False)
    token = Column(String, nullable=False, unique=True)
