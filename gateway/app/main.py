from fastapi import FastAPI

app = FastAPI(
    title="Quiz API Gateway"
)


@app.get("/")
def root():
    return {
        "service": "API Gateway",
        "status": "running"
    }