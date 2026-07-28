from fastapi import FastAPI

from app.core.database import Base, engine
import app
from app.api.v1.auth import router as auth_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="InterviewProAI",
    version="0.1.0"
)
app.include_router(auth_router)
@app.get("/")
def home():
    return {
        "message": "Welcome to InterviewProAI Backend"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }