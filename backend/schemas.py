from pydantic import BaseModel
from datetime import datetime

class UserCreate(BaseModel):
    email: str
    password: str

class UserResponse(BaseModel):
    id: int
    email: str

    class Config:
        orm_mode = True

class ReadingCreate(BaseModel):
    bloodSugar: int
    bloodPressure: int
    user_email: str

class ReadingResponse(BaseModel):
    id: int
    date: datetime
    bloodSugar: int
    bloodPressure: int
    user_email: str

    class Config:
        orm_mode = True
