from pydantic import BaseModel

class AnswerCreate(BaseModel):
    answer: str
    is_correct: bool
    
class AnswerResponse(BaseModel):
    id: int
    answer: str
    is_correct: bool

    class Config:
        from_attributes = True


class QuestionCreate(BaseModel):
    question: str
    answers: list[AnswerCreate]
    
class QuestionResponse(BaseModel):
    id: int
    question: str
    answers: list[AnswerResponse]

    class Config:
        from_attributes = True