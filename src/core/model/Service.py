from sqlalchemy import Column, Integer, String, Float

from src.core.config.database import Base


class Service(Base):
    __tablename__ = "service"
    service_id = Column(Integer, primary_key=True, autoincrement=True)
    nom = Column(String(50))
    description = Column(String(255))
    prix = Column(Float)
