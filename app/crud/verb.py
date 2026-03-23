from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import func

from app.database.models import IrregularVerb


def get_all_verbs(db: Session):
    return db.query(IrregularVerb).all()


def get_verb_by_id(db: Session, verb_id: int):
    return db.query(IrregularVerb).filter(IrregularVerb.id == verb_id).first()

def get_verbs_by_level(db: Session, level: str):
    return db.query(IrregularVerb).filter(IrregularVerb.level == level).all()

def get_random_verb(db: Session):
    return db.query(IrregularVerb).order_by(func.random()).first()


def get_random_verb_by_level(db: Session, level: str):
    return (
        db.query(IrregularVerb)
        .filter(IrregularVerb.level == level)
        .order_by(func.random())
        .first()
    )

