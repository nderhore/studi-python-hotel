from sqlalchemy import String, Column

from src.core.config.database import Base


class User(Base):
    __tablename__ = "user"
    username = Column(String, primary_key=True)
    password = Column(String)
