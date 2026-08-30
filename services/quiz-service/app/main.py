from fastapi import FastAPI
from .database import engine, Base
from . import models
from .routes.questions import router as questions_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Quiz Service",
    description="Mikroservis za upravljanje kvizovima i pitanjima",
    version="1.0.0"
)

app.include_router(questions_router)

@app.get("/")
def root():
    return {"service": "Quiz Service", "status": "running"}