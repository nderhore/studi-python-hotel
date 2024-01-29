from fastapi import APIRouter

from src.api.endpoint import (
    Auth_endpoint,
    Chambre_endpoint,
    Client_endpoint,
    Reservation_endpoint,
)

router = APIRouter()

router.include_router(
    Auth_endpoint.router,
    prefix="/auth",
    tags=["auth"],
    responses={404: {"description": "Not found"}},
)

router.include_router(
    Chambre_endpoint.router,
    prefix="/chambre",
    tags=["chambre"],
    responses={404: {"description": "Not found"}},
)

router.include_router(
    Client_endpoint.router,
    prefix="/client",
    tags=["client"],
    responses={404: {"description": "Not found"}},
)

router.include_router(
    Reservation_endpoint.router,
    prefix="/reservation",
    tags=["reservation"],
    responses={404: {"description": "Not found"}},
)

router.include_router(
    Reservation_endpoint.router,
    prefix="/reservation",
    tags=["reservation"],
    responses={404: {"description": "Not found"}},
)
