from datetime import datetime as datetime

from pydantic import BaseModel


class ReservationSchemasBase(BaseModel):
    client_id: int
    chambre_id: int
    date_arrivee: datetime
    date_depart: datetime
    prix_total: float


class ReservationSchemas(ReservationSchemasBase):
    reservation_id: int

    class Config:
        orm_mode = True
