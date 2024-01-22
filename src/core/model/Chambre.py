from sqlalchemy import Column, Float, Integer, String

from src.core.config.database import Base


class Chambre(Base):
    __tablename__ = "chambre"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nom = Column(String)
    tarif = Column(Float)
    capacite = Column(Integer)
