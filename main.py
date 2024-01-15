from fastapi import FastAPI

from src.core.config.database import Base, engine

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


# Créer les tables dans la BDD
Base.metadata.create_all(bind=engine)
