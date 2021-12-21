from sqlalchemy.sql.expression import text, true
from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.sql.sqltypes import JSON, TIMESTAMP, Integer, String, TEXT
from storage.database import Base


class Business(Base):
    __tablename__ = "businesses"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False, unique=True)
    description = Column(TEXT, nullable=False)
    domain = Column(JSON, nullable=False)
    contacts = Column(JSON, nullable=False)
    email = Column(String, nullable=False, unique=True)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False,
                        server_default=text('now()')
                        )
    updated_at = Column(TIMESTAMP(timezone=True),
                        nullable=False,
                        server_default=text('now()')
                        )
    user_id = Column(Integer,
                     ForeignKey("users.id", ondelete="CASCADE"),
                     nullable=False
                     )
