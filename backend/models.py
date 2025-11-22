from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship, declarative_base
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    # Set a max length for email to avoid unlimited string size
    email = Column(String(255), unique=True, index=True, nullable=False)
    # Passwords are hashed, so allow enough length
    password = Column(String(255), nullable=False)

    # Relationship to health readings
    readings = relationship("HealthReading", back_populates="owner", cascade="all, delete-orphan")

class HealthReading(Base):
    __tablename__ = "health_readings"

    id = Column(Integer, primary_key=True, index=True)
    # Use DateTime instead of Date for more flexibility (date + time)
    date = Column(DateTime, default=datetime.utcnow, nullable=False)
    bloodSugar = Column(Integer, nullable=False)
    bloodPressure = Column(Integer, nullable=False)

    # Foreign key linking to User
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    owner = relationship("User", back_populates="readings")
