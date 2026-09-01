from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from .database import Base


class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    question = Column(String, nullable=False)
    answers = relationship(
        "Answer",
        back_populates="question",
        cascade="all, delete-orphan"
    )

class Answer(Base):
    __tablename__ = "answers"

    id = Column(Integer, primary_key=True, index=True)
    answer = Column(String, nullable=False)
    is_correct = Column(Boolean, default=False)

    question_id = Column(
        Integer,
        ForeignKey("questions.id"),
        nullable=False
    )

    question = relationship(
        "Question",
        back_populates="answers"
    )
    
class PlayerAnswer(Base):
    __tablename__ = "player_answers"

    id = Column(Integer, primary_key=True, index=True)

    player_id = Column(Integer, nullable=False, index=True)

    question_id = Column(
        Integer,
        ForeignKey("questions.id"),
        nullable=False
    )

    answer_id = Column(
        Integer,
        ForeignKey("answers.id"),
        nullable=False
    )

    is_correct = Column(Boolean, nullable=False)

    __table_args__ = (
        UniqueConstraint(
            "player_id",
            "question_id",
            name="unique_player_question"
        ),
    )