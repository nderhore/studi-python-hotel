from fastapi import APIRouter, Depends

from src.core.config.database import get_db
from src.core.controller import Chambre_controller
from src.core.schemas.Chambre_schemas import ChambreSchemasBase, ChambreSchemas

router = APIRouter()


# creation de chambre
@router.post(response_model=ChambreSchemas)
async def create_chambre(chambre: ChambreSchemasBase, db=Depends(get_db)):
    chambre: ChambreSchemas = await Chambre_controller.create_chambre(db, chambre)
    return chambre


# suppression d'une chambre
@router.delete("/{chambre_id}")
async def delete_chambre(chambre_id: int, db=Depends(get_db)):
    await Chambre_controller.delete_chambre_by_id(db, chambre_id)


# modification d'une chambre


@router.put("/{chambre_id}", response_model=ChambreSchemas | dict)
async def update_chambre(
    chambre_id: int, chambre: ChambreSchemasBase, db=Depends(get_db)
):
    chambre_return = await Chambre_controller.update_chambre(db, chambre_id, chambre)
    return chambre_return


# renvoyer toutes les chambres
@router.get("/", response_model=list[ChambreSchemas])
async def get_chambre(db=Depends(get_db)):
    chambre_list = await Chambre_controller.get_chambre(db)
    return chambre_list


# renvoyer une chambre
@router.get("/{chambre_id}")
async def get_chambre_by_id(chambre_id: int, db=Depends(get_db)):
    chambre = await Chambre_controller.get_chambre_by_id(chambre_id)
    return chambre
