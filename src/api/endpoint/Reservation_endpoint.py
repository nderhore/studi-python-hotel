from fastapi import APIRouter, Depends

from src.core.config.database import get_db
from src.core.controller.Reservation_controller import get_reservations_by_client_id
from src.core.schemas.Reservation_schemas import ReservationSchemasBase

router = APIRouter()


@router.get("/{client_id}", response_model=list[ReservationSchemasBase])
async def get_reservations_by_client_id(client_id: int, db=Depends(get_db)):
    reservations: list[ReservationSchemasBase] = await get_reservations_by_client_id(
        client_id=client_id, db=db
    )
    return reservations
