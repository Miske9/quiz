from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import Question, Answer
from ..schemas import *

router = APIRouter(
    prefix="/questions",
    tags=["Questions"]
)

@router.get("/")
def get_questions(db: Session = Depends(get_db)):
  questions = db.query(Question).all()
  
  result = []

  for question in questions:
      result.append({
          "id": question.id,
          "question": question.question,
          "answers": [
              {
                  "id": answer.id,
                  "answer": answer.answer,
                  "is_correct": answer.is_correct
              }
              for answer in question.answers
          ]
      })

  return result


@router.get("/{question_id}", response_model=QuestionResponse)
def get_question(question_id: int, db: Session = Depends(get_db)):
    question = db.query(Question).filter(Question.id == question_id).first()

    if not question:
        raise HTTPException(
            status_code=404,
            detail="Question not found"
        )

    return question
  

@router.post("/")
def create_question(
    question_data: QuestionCreate,
    db: Session = Depends(get_db)
):
    question = Question(
        question=question_data.question
    )

    for answer_data in question_data.answers:
        answer = Answer(
            answer=answer_data.answer,
            is_correct=answer_data.is_correct
        )

        question.answers.append(answer)

    db.add(question)
    db.commit()
    db.refresh(question)

    return question

  
@router.put("/{question_id}", response_model=QuestionResponse)
def update_question(
    question_id: int,
    question_data: QuestionCreate,
    db: Session = Depends(get_db)
):
    question = db.query(Question).filter(
        Question.id == question_id
    ).first()

    if not question:
        raise HTTPException(
            status_code=404,
            detail="Question not found"
        )

    question.question = question_data.question

    question.answers.clear()

    for answer_data in question_data.answers:
        answer = Answer(
            answer=answer_data.answer,
            is_correct=answer_data.is_correct
        )

        question.answers.append(answer)

    db.commit()
    db.refresh(question)

    return question


@router.delete("/{question_id}")
def delete_question(
    question_id: int,
    db: Session = Depends(get_db)
):
    question = db.query(Question).filter(
        Question.id == question_id
    ).first()

    if not question:
        raise HTTPException(
            status_code=404,
            detail="Question not found"
        )

    db.delete(question)
    db.commit()

    return {
        "message": "Question deleted successfully"
    }