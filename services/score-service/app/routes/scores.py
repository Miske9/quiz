from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import httpx

from ..database import get_db
from ..models import Score
from ..schemas import ScoreCreate, ScoreResponse

router = APIRouter(
    prefix="/scores",
    tags=["Scores"]
)


@router.post("/", response_model=ScoreResponse)
def create_score(
    score_data: ScoreCreate,
    db: Session = Depends(get_db)
):
    score = db.query(Score).filter(
        Score.player_id == score_data.player_id
    ).first()

    if score:
        score.points += score_data.points
    else:
        score = Score(
            player_id=score_data.player_id,
            points=score_data.points
        )
        db.add(score)

    db.commit()
    db.refresh(score)

    return score
  

@router.get("/", response_model=list[ScoreResponse])
def get_scores(db: Session = Depends(get_db)):
    return db.query(Score).order_by(
        Score.points.desc()
    ).all()
    

@router.get("/leaderboard")
def get_leaderboard(db: Session = Depends(get_db)):
    scores = db.query(Score).order_by(
        Score.points.desc()
    ).all()

    leaderboard = []

    for score in scores:
        try:
            response = httpx.get(
                f"http://player-service:8001/players/{score.player_id}"
            )

            if response.status_code == 200:
                player = response.json()

                leaderboard.append({
                    "player_id": score.player_id,
                    "username": player["username"],
                    "points": score.points
                })

        except Exception:
            continue

    return leaderboard

@router.delete("/{player_id}")
def reset_score(
    player_id: int,
    db: Session = Depends(get_db)
):
    score = db.query(Score).filter(
        Score.player_id == player_id
    ).first()

    if not score:
        return {
            "message": "Score not found"
        }

    db.delete(score)
    db.commit()

    return {
        "message": "Score reset successfully",
        "player_id": player_id
    }