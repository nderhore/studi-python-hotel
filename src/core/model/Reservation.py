from sqlalchemy import Integer, Column, ForeignKey, Date, Float
from sqlalchemy.orm import relationship

from src.core.config.database import Base


class Reservation(Base):
    __tablename__ = "reservation"
    reservation_id = Column(Integer, index=True)
    client_id = Column(Integer, ForeignKey("client.client_id"))
    chambre_id = Column(Integer, ForeignKey("chambre.chambre_id"))
    date_arrivee = Column(Date)
    date_depart = Column(Date)
    prix_total = Column(Float)
    client = relationship("Client")
    chambe = relationship("Chambre")
