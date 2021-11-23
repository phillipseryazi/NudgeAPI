from sqlalchemy.sql.sqltypes import Integer
from storage.database import Base
from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import String, Integer, TIMESTAMP
from sqlalchemy.sql.expression import text


class Profile(Base):
    __tablename__ = "profiles"
    id = Column(Integer, primary_key=True, nullable=False)
    firstname = Column(String, nullable=True)
    lastname = Column(String, nullable=True)
    phone_number = Column(String, nullable=True)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))
