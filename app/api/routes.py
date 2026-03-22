from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.crud.verb import get_all_verbs, get_verb_by_id, get_verbs_by_level
from app.database.db import get_db
from app.schemas.verb import VerbResponse

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