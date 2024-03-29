from sqlalchemy import Column, Date, Float, ForeignKey, Integer, PrimaryKeyConstraint

from src.core.config.database import Base


class Reservation(Base):
    __tablename__ = "reservation"
    reservation_id = Column(Integer, index=True)
    client_id = Column(Integer, ForeignKey("client.client_id"))
    chambre_id = Column(Integer, ForeignKey("chambre.chambre_id"))
    date_arrivee = Column(Date)
    date_depart = Column(Date)
    prix_total = Column(Float)

    __table_args__ = (
        PrimaryKeyConstraint("reservation_id", "client_id", "chambre_id"),
    )
