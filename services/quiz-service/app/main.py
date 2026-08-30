from fastapi import FastAPI

app = FastAPI(
    title="Quiz Service",
    description="Mikroservis za upravljanje kvizovima i pitanjima",
    version="1.0.0"
)


questions = [
    {
        "id": 1,
        "question": "Koji je glavni grad Hrvatske?",
        "answers": ["Zagreb", "Split", "Rijeka", "Osijek"],
        "correct_answer": "Zagreb"
    },
    {
        "id": 2,
        "question": "Koliko kontinenata postoji?",
        "answers": ["5", "6", "7", "8"],
        "correct_answer": "7"
    }
]


@app.get("/")
def root():
    return {"service": "Quiz Service", "status": "running"}


@app.get("/questions")
def get_questions():
    return questions


@app.get("/questions/{question_id}")
def get_question(question_id: int):
    for question in questions:
        if question["id"] == question_id:
            return question

    return {"error": "Question not found"}