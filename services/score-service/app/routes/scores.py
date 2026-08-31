from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

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