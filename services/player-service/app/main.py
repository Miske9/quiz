from fastapi import FastAPI

from .database import Base, engine
from . import models
from .routes.players import router as players_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Player Service",
    description="Mikroservis za upravljanje igračima",
    version="1.0.0"
)

app.include_router(players_router)

@app.get("/")
def root():
    return {"service": "Player Service", "status": "running"}