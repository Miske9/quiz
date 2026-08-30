from sqlalchemy import Column, Integer, String
from .database import Base


class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    question = Column(String, nullable=False)
    answers = Column(String, nullable=False)
    correct_answer = Column(String, nullable=False)