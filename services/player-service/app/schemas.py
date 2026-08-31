from pydantic import BaseModel


class PlayerCreate(BaseModel):
    username: str


class PlayerResponse(BaseModel):
    id: int
    username: str

    class Config:
        from_attributes = True