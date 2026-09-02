from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import httpx

app = FastAPI(
    title="Quiz API Gateway"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

QUIZ_SERVICE_URL = "http://quiz-service:8000"
PLAYER_SERVICE_URL = "http://player-service:8001"
SCORE_SERVICE_URL = "http://score-service:8002"

class AnswerSubmit(BaseModel):
    player_id: int
    answer_id: int

class PlayerCreate(BaseModel):
    username: str

class ScoreCreate(BaseModel):
    player_id: int
    points: int

class AnswerCreate(BaseModel):
    answer: str
    is_correct: bool

class QuestionCreate(BaseModel):
    question: str
    answers: list[AnswerCreate]

class PlayersDelete(BaseModel):
    player_ids: list[int]

@app.get("/")
def root():
    return {
        "service": "API Gateway",
        "status": "running"
    }
    
@app.get("/questions")
def get_questions(player_id: int):
    try:
        response = httpx.get(
            f"{QUIZ_SERVICE_URL}/questions/",
            params={
                "player_id": player_id
            }
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
        
@app.post("/questions")
def create_question(question_data: QuestionCreate):
    try:
        response = httpx.post(
            f"{QUIZ_SERVICE_URL}/questions/",
            json=question_data.model_dump()
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


@app.get("/players")
def get_players():
    try:
        response = httpx.get(
          f"{PLAYER_SERVICE_URL}/players/"
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
        

@app.post("/players")
def create_player(player_data: PlayerCreate):
    try:
        response = httpx.post(
            f"{PLAYER_SERVICE_URL}/players/",
            json=player_data.model_dump()
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

@app.get("/scores/leaderboard")
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
        
@app.get("/scores")
def get_scores():
    try:
        response = httpx.get(
            f"{SCORE_SERVICE_URL}/scores/"
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


@app.post("/scores")
def create_score(score_data: ScoreCreate):
    try:
        response = httpx.post(
            f"{SCORE_SERVICE_URL}/scores/",
            json=score_data.model_dump()
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
        
@app.delete("/players/{player_id}/reset")
def reset_player(player_id: int):
    try:
        quiz_response = httpx.delete(
            f"{QUIZ_SERVICE_URL}/questions/player/{player_id}/reset",
            timeout=5.0
        )

        if quiz_response.status_code != 200:
            raise HTTPException(
                status_code=quiz_response.status_code,
                detail="Quiz reset error"
            )

        score_response = httpx.delete(
            f"{SCORE_SERVICE_URL}/scores/{player_id}",
            timeout=5.0
        )

        if score_response.status_code != 200:
            raise HTTPException(
                status_code=score_response.status_code,
                detail="Score reset error"
            )

        return {
            "message": "Player reset successfully",
            "player_id": player_id
        }

    except httpx.RequestError:
        raise HTTPException(
            status_code=503,
            detail="Service unavailable"
        )
        
@app.delete("/players")
def delete_players(data: PlayersDelete):
    try:
        player_response = httpx.request(
            "DELETE",
            f"{PLAYER_SERVICE_URL}/players/",
            json=data.player_ids,
            timeout=5.0
        )

        if player_response.status_code != 200:
            raise HTTPException(
                status_code=player_response.status_code,
                detail="Player delete error"
            )

        for player_id in data.player_ids:
            quiz_response = httpx.delete(
                f"{QUIZ_SERVICE_URL}/questions/player/{player_id}/reset",
                timeout=5.0
            )

            if quiz_response.status_code != 200:
                raise HTTPException(
                    status_code=quiz_response.status_code,
                    detail="Quiz delete error"
                )

            score_response = httpx.delete(
                f"{SCORE_SERVICE_URL}/scores/{player_id}",
                timeout=5.0
            )

            if score_response.status_code != 200:
                raise HTTPException(
                    status_code=score_response.status_code,
                    detail="Score delete error"
                )

        return {
            "message": "Players deleted successfully",
            "player_ids": data.player_ids
        }

    except httpx.RequestError:
        raise HTTPException(
            status_code=503,
            detail="Service unavailable"
        )