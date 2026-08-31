from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..database import get_db
from ..models import Player
from ..schemas import PlayerCreate, PlayerResponse

router = APIRouter(
    prefix="/players",
    tags=["Players"]
)


@router.post("/", response_model=PlayerResponse)
def create_player(
    player_data: PlayerCreate,
    db: Session = Depends(get_db)
):
    player = Player(
        username=player_data.username
    )

    db.add(player)
    db.commit()
    db.refresh(player)

    return player