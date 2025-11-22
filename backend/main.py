from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from models import Base, User, HealthReading
from auth import create_user, authenticate_user
from schemas import UserCreate, ReadingCreate, ReadingResponse, UserResponse
from datetime import datetime
from typing import List

DATABASE_URL = "sqlite:///./database.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency for DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ------------------- ROUTES -------------------

@app.post("/signup", response_model=UserResponse)
def signup(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    new_user = create_user(db, user.email, user.password)
    return {"id": new_user.id, "email": new_user.email}

@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    return {"access_token": user.email, "token_type": "bearer"}

@app.post("/add-reading", response_model=ReadingResponse)
def add_reading(reading: ReadingCreate, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == reading.user_email).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    new_reading = HealthReading(
        date=datetime.utcnow(),
        bloodSugar=reading.bloodSugar,
        bloodPressure=reading.bloodPressure,
        owner=user
    )
    db.add(new_reading)
    db.commit()
    db.refresh(new_reading)
    return {
        "id": new_reading.id,
        "date": new_reading.date,
        "bloodSugar": new_reading.bloodSugar,
        "bloodPressure": new_reading.bloodPressure,
        "user_email": user.email
    }

@app.get("/readings", response_model=List[ReadingResponse])
def get_readings(user_email: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == user_email).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return [
        {
            "id": r.id,
            "date": r.date,
            "bloodSugar": r.bloodSugar,
            "bloodPressure": r.bloodPressure,
            "user_email": user.email
        }
        for r in user.readings
    ]
