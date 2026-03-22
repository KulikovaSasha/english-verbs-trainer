from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.crud.verb import get_all_verbs, get_verb_by_id, get_verbs_by_level
from app.database.db import get_db
from app.schemas.verb import (
    TrainingAnswerRequest,
    TrainingCheckResponse,
    TrainingTaskResponse,
    VerbResponse,
)
from app.services.trainer import check_training_answer, get_training_task

router = APIRouter()


@router.get("/verbs", response_model=list[VerbResponse])
def read_verbs(db: Session = Depends(get_db)):
    return get_all_verbs(db)


@router.get("/verbs/by-level/{level}", response_model=list[VerbResponse])
def read_verbs_by_level(level: str, db: Session = Depends(get_db)):
    return get_verbs_by_level(db, level)


@router.get("/verbs/{verb_id}", response_model=VerbResponse)
def read_verb(verb_id: int, db: Session = Depends(get_db)):
    verb = get_verb_by_id(db, verb_id)

    if verb is None:
        raise HTTPException(status_code=404, detail="Verb not found")

    return verb


@router.get("/train/task", response_model=TrainingTaskResponse)
def read_training_task(db: Session = Depends(get_db)):
    task = get_training_task(db)

    if task is None:
        raise HTTPException(status_code=404, detail="No verbs available")

    return task


@router.post("/train/check", response_model=TrainingCheckResponse)
def check_answer(data: TrainingAnswerRequest, db: Session = Depends(get_db)):
    result = check_training_answer(
        db=db,
        user_id=data.user_id,
        verb_id=data.verb_id,
        past_simple=data.past_simple,
        past_participle=data.past_participle,
    )

    if result is None:
        raise HTTPException(status_code=404, detail="Verb not found")

    return result