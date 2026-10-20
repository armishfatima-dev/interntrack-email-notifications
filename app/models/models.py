from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(String, default="intern") # intern, mentor, admin

    submissions = relationship("Submission", back_populates="intern")

class Submission(Base):
    __tablename__ = "submissions"

    id = Column(Integer, primary_key=True, index=True)
    intern_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    week = Column(Integer, nullable=False)
    content = Column(Text, nullable=False)
    grade = Column(String, nullable=True)
    feedback = Column(Text, nullable=True)

    intern = relationship("User", back_populates="submissions")

