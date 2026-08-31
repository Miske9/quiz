from fastapi import FastAPI

from .database import Base, engine
from . import models


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Score Service",
    description="Mikroservis za upravljanje rezultatima",
    version="1.0.0"
)


@app.get("/")
def root():
    return { "service": "Score Service", "status": "running"}