from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import httpx

app = FastAPI(
    title="Quiz API Gateway"
)

QUIZ_SERVICE_URL = "http://quiz-service:8000"
PLAYER_SERVICE_URL = "http://player-service:8001"
SCORE_SERVICE_URL = "http://score-service:8002"

class AnswerSubmit(BaseModel):
    player_id: int
    answer_id: int

@app.get("/")
def root():
    return {
        "service": "API Gateway",
        "status": "running"
    }
    
@app.get("/questions")
def get_questions():
    try:
        response = httpx.get(
            f"{QUIZ_SERVICE_URL}/questions/"
        )

        if response.status_code != 200:
            raise HTTPException(
                status_code=response.status_code,
                detail="Quiz service error"
            )

        return response.json()

    except httpx.RequestError:
        raise HTTPException(
            status_code=503,
            detail="Quiz service unavailable"
        )
        

@app.get("/players/{player_id}")
def get_player(player_id: int):
    try:
        response = httpx.get(
            f"{PLAYER_SERVICE_URL}/players/{player_id}"
        )

        if response.status_code != 200:
            raise HTTPException(
                status_code=response.status_code,
                detail="Player service error"
            )

        return response.json()

    except httpx.RequestError:
        raise HTTPException(
            status_code=503,
            detail="Player service unavailable"
        )
        

@app.get("/leaderboard")
def get_leaderboard():
    try:
        response = httpx.get(
            f"{SCORE_SERVICE_URL}/scores/leaderboard"
        )

        if response.status_code != 200:
            raise HTTPException(
                status_code=response.status_code,
                detail="Score service error"
            )

        return response.json()

    except httpx.RequestError:
        raise HTTPException(
            status_code=503,
            detail="Score service unavailable"
        )
        
@app.post("/questions/{question_id}/answer")
def submit_answer(
    question_id: int,
    answer_data: AnswerSubmit
):
    try:
        response = httpx.post(
            f"{QUIZ_SERVICE_URL}/questions/{question_id}/answer",
            json=answer_data.model_dump()
        )

        if response.status_code != 200:
            raise HTTPException(
                status_code=response.status_code,
                detail="Quiz service error"
            )

        return response.json()

    except httpx.RequestError:
        raise HTTPException(
            status_code=503,
            detail="Quiz service unavailable"
        )