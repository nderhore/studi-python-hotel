from dotenv import load_dotenv
from fastapi import FastAPI
from sqlalchemy import text
from starlette.middleware.cors import CORSMiddleware

from src.api import api
from src.core.config.database import Base, engine
from src.core.model.Chambre import Chambre
from src.core.model.Client import Client
from src.core.model.Reservation import Reservation
from src.core.model.Service import Service

load_dotenv()
app = FastAPI()

app.include_router(api.router, prefix="/api")


def drop_and_create_database():
    # Supprimer toutes les tables
    Base.metadata.drop_all(bind=engine)

    # Recréer toutes les tables
    Base.metadata.create_all(
        bind=engine,
        tables=[
            Service.__table__,
            Chambre.__table__,
            Client.__table__,
            Reservation.__table__,
        ],
    )

    # Exécuter le contenu du fichier SQL
    with engine.connect() as connection:
        with open("import.sql", "r") as file:
            # Lire le contenu du fichier et supprimer les sauts de ligne
            sql_content = " ".join(
                line.strip() for line in file if not line.strip().startswith("--")
            )

            # Diviser les déclarations SQL en utilisant le point-virgule comme séparateur
            sql_statements = sql_content.split(";")

            # Supprimer les espaces vides et les lignes vides
            sql_statements = [
                statement.strip() for statement in sql_statements if statement.strip()
            ]

            # Exécutez chaque déclaration SQL en utilisant l'Engine
            for statement in sql_statements:
                connection.execute(text(statement))
        connection.commit()


@app.on_event("startup")
async def startup_event():
    drop_and_create_database()


app.add_middleware(
    CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=[""]
)
