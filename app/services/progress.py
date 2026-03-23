from sqlalchemy.orm import Session

from app.crud.progress import get_level_progress


def get_user_level_progress(db: Session, user_id: int, level: str):
    return get_level_progress(db, user_id, level)
