from sqlalchemy.orm import Session
from starlette import status
from starlette.responses import JSONResponse

from src.core.model.Chambre import Chambre
from src.core.schemas.Chambre_schemas import ChambreSchemas, ChambreSchemasBase


async def create_chambre(db: Session, chambre: ChambreSchemasBase) -> ChambreSchemas:
    db.add(chambre)
    db.commit()
    db.refresh(chambre)
    return ChambreSchemas(
        id=chambre.id, nom=chambre.com, tarif=chambre.tarif, capacite=chambre.capacite
    )


async def delete_chambre_by_id(db: Session, chambre_id: int):
    db.delete(Chambre).filter(Chambre.id == chambre_id)
    db.commit()


async def get_chambre_by_id(db: Session, chambre_id: int) -> ChambreSchemas:
    chambre: Chambre = db.query(Chambre).filter(Chambre.id == chambre_id).first()
    return ChambreSchemas(
        id=chambre.id, nom=chambre.com, tarif=chambre.tarif, capacite=chambre.capacite
    )


async def get_chambre(db: Session) -> list[ChambreSchemas]:
    list_chambre: list[ChambreSchemas] = []
    chambre_db = db.query(Chambre).all()
    for chambre in chambre_db:
        list_chambre.append(
            ChambreSchemas(
                id=chambre.id,
                nom=chambre.com,
                tarif=chambre.tarif,
                capacite=chambre.capacite,
            )
        )
    return list_chambre


async def update_chambre(
    db: Session, chambre_id: int, chambre: ChambreSchemasBase
) -> ChambreSchemas | dict:
    # 1. retrouver la chambre en base
    chambre_db = db.query(Chambre).filter(Chambre.id == chambre_id)
    # 2. modifier les proprietes
    if chambre_db is not None:
        chambre_db.nom = chambre.nom
        chambre_db.tarif = chambre.tarif
        chambre_db.capacite = chambre.capacite
        db.add(chambre_db)
        db.commit()
        db.refresh(chambre_db)
    else:
        return JSONResponse(
            content="id of the chambre, doesn't exist.",
            status_code=status.HTTP_400_BAD_REQUEST,
        ).__dict__
