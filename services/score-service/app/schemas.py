from pydantic import BaseModel

class ScoreCreate(BaseModel):
    player_id: int
    points: int


class ScoreResponse(BaseModel):
    id: int
    player_id: int
    points: int

    class Config:
        from_attributes = True