import os
from sqlalchemy import create_engine
from sqlalchemy.orm import session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DB_URL = os.environ.get("DATABASE_URL").replace("postgres://", "postgresql://", 1)
engine=create_engine(DB_URL)
SessionLocal=sessionmaker(autocommit = False, autoflush = False, bind = engine)
Base=declarative_base()


def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()
