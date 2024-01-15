from pydantic import BaseModel


class ChambreSchemasBase(BaseModel):
    nom: str
    tarif: float
    capacite: int


class ChambreSchemas(ChambreSchemasBase):
    id : int

    class Config:
        orm_mode = True