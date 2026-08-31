from fastapi import FastAPI

from .database import Base, engine
from . import models
from .routes.scores import router as scores_router


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Score Service",
    description="Mikroservis za upravljanje rezultatima",
    version="1.0.0"
)

app.include_router(scores_router)

@app.get("/")
def root():
    return { "service": "Score Service", "status": "running"}