from sqlalchemy import Column, Integer, String

from src.core.config.database import Base


class Client(Base):
    __tablename__ = "client"
    client_id = Column(Integer, primary_key=True, autoincrement=True)
    nom = Column(String(50))
    prenom = Column(String(50))
    email = Column(String(50))
    telephone = Column(String(10))
