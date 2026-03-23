from sqlalchemy.orm import Session

from app.database.models import User


def get_user_by_telegram_id(db: Session, telegram_id: str):
    return db.query(User).filter(User.telegram_id == telegram_id).first()


def create_user(db: Session, telegram_id: str, username: str | None = None):
    user = User(
        telegram_id=telegram_id,
        username=username,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_or_create_user(db: Session, telegram_id: str, username: str | None = None):
    user = get_user_by_telegram_id(db, telegram_id)

    if user is None:
        user = create_user(db, telegram_id, username)

    return user