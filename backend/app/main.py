from fastapi import FastAPI, Depends
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.core.database import get_db, Base, engine
from app.models.user import User


app = FastAPI(
    title="GeM Compliance AI Backend",
    description="AI-Powered Integrated Bid Compliance Verification Platform",
    version="1.0.0"
)

Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {
        "message": "GeM Compliance AI Backend is running!"
    }


@app.get("/health")
def health_check(db: Session = Depends(get_db)):

    db.execute(text("SELECT 1"))

    return {
        "status": "healthy",
        "database": "connected"
    }
from fastapi import FastAPI
from app.routes.auth import router as auth_router

app = FastAPI(
    title="GeM Compliance AI"
)

app.include_router(auth_router)


@app.get("/")
def root():
    return {
        "message": "GeM Compliance AI Backend is running"
    }