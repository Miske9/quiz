import httpx
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func
from ..database import get_db
from ..models import *
from ..schemas import *

router = APIRouter(
    prefix="/questions",
    tags=["Questions"]
)

@router.get("/")
def get_questions(
    player_id: int,
    db: Session = Depends(get_db)
):
    answered_question_ids = db.query(
        PlayerAnswer.question_id
    ).filter(
        PlayerAnswer.player_id == player_id
    ).all()

    answered_question_ids = [
        question_id
        for (question_id,) in answered_question_ids
    ]

    query = db.query(Question)

    if answered_question_ids:
        query = query.filter(
            ~Question.id.in_(answered_question_ids)
        )

    questions = query.order_by(
        func.random()
    ).limit(15).all()

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

@router.delete("/player/{player_id}/reset")
def reset_player_answers(
    player_id: int,
    db: Session = Depends(get_db)
):
    deleted_answers = db.query(PlayerAnswer).filter(
        PlayerAnswer.player_id == player_id
    ).delete(synchronize_session=False)

    db.commit()

    return {
        "message": "Player answers reset successfully",
        "player_id": player_id,
        "deleted_answers": deleted_answers
    }

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


@router.post("/{question_id}/answer", response_model=AnswerResult)
def submit_answer(
    question_id: int,
    answer_data: AnswerSubmit,
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

    existing_answer = db.query(PlayerAnswer).filter(
        PlayerAnswer.player_id == answer_data.player_id,
        PlayerAnswer.question_id == question_id
    ).first()

    if existing_answer:
        correct_answer = next(
            answer for answer in question.answers
            if answer.is_correct
        )

        return {
            "correct": existing_answer.is_correct,
            "correct_answer": correct_answer.answer,
            "points": 0
        }

    answer = db.query(Answer).filter(
        Answer.id == answer_data.answer_id,
        Answer.question_id == question_id
    ).first()

    if not answer:
        raise HTTPException(
            status_code=404,
            detail="Answer not found"
        )

    correct_answer = next(
        answer for answer in question.answers
        if answer.is_correct
    )

    if answer.is_correct:
        correct = True
        points = 1
    else:
        correct = False
        points = 0

    player_answer = PlayerAnswer(
        player_id=answer_data.player_id,
        question_id=question_id,
        answer_id=answer_data.answer_id,
        is_correct=correct
    )

    db.add(player_answer)
    db.commit()

    try:
        response = httpx.post(
            "http://score-service:8002/scores/",
            json={
                "player_id": answer_data.player_id,
                "points": points
            },
            timeout=5.0
        )

        response.raise_for_status()

    except httpx.HTTPError:
        raise HTTPException(
            status_code=503,
            detail="Score service unavailable"
        )

    return {
        "correct": correct,
        "correct_answer": correct_answer.answer,
        "points": points
    }
  
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