from sqlalchemy.orm import Session

from src.core.model.Reservation import Reservation
from src.core.schemas.Reservation_schemas import (
    ReservationSchemasBase,
    ReservationSchemas,
)


async def get_reservations_by_client_id(
    client_id: int, db: Session
) -> list[ReservationSchemasBase]:
    reservations_bdd: list[Reservation] = (
        db.query(Reservation).filter(Reservation.client_id == client_id).all()
    )
    reservation_schemas: list[ReservationSchemasBase] = []
    for reservation in reservations_bdd:
        reservation_schemas.append(ReservationSchemas(**reservation.dict()))
    return reservation_schemas
