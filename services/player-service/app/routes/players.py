from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..database import get_db
from ..models import Player
from ..schemas import PlayerCreate, PlayerResponse

router = APIRouter(
    prefix="/players",
    tags=["Players"]
)

@router.get("/", response_model=list[PlayerResponse])
def get_players(db: Session = Depends(get_db)):
    return db.query(Player).all()


@router.get("/{player_id}", response_model=PlayerResponse)
def get_player(player_id: int, db: Session = Depends(get_db)):
    player = db.query(Player).filter(
        Player.id == player_id
    ).first()

    if not player:
        raise HTTPException(
            status_code=404,
            detail="Player not found"
        )

    return player

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

@router.delete("/")
def delete_players(
    player_ids: list[int],
    db: Session = Depends(get_db)
):
    deleted_players = db.query(Player).filter(
        Player.id.in_(player_ids)
    ).delete(synchronize_session=False)

    db.commit()

    return {
        "message": "Players deleted successfully",
        "deleted_players": deleted_players
    }