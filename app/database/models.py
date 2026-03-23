from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.database.db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    telegram_id = Column(String, unique=True, nullable=True)
    username = Column(String, nullable=True)
    score = Column(Integer, default=0)

    results = relationship("TrainingResult", back_populates="user")
    progress = relationship("UserProgress", back_populates="user")


class IrregularVerb(Base):
    __tablename__ = "irregular_verbs"

    id = Column(Integer, primary_key=True)
    base_form = Column(String, nullable=False)
    past_simple = Column(String, nullable=False)
    past_participle = Column(String, nullable=False)
    translation = Column(String, nullable=False)
    level = Column(String, default="A0")

    results = relationship("TrainingResult", back_populates="verb")
    progress = relationship("UserProgress", back_populates="verb")


class TrainingResult(Base):
    __tablename__ = "training_results"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    verb_id = Column(Integer, ForeignKey("irregular_verbs.id"))
    user_answer = Column(String, nullable=False)
    correct_answer = Column(String, nullable=False)
    is_correct = Column(Boolean, default=False)

    user = relationship("User", back_populates="results")
    verb = relationship("IrregularVerb", back_populates="results")


class UserProgress(Base):
    __tablename__ = "user_progress"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    verb_id = Column(Integer, ForeignKey("irregular_verbs.id"))
    correct_count = Column(Integer, default=0)
    wrong_count = Column(Integer, default=0)

    user = relationship("User", back_populates="progress")
    verb = relationship("IrregularVerb", back_populates="progress")