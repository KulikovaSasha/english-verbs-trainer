from sqlalchemy import desc, func
from sqlalchemy.orm import Session

from app.database.models import IrregularVerb, TrainingResult, UserProgress


def get_user_training_stats(db: Session, user_id: int):
    total_answers = (
        db.query(func.count(TrainingResult.id))
        .filter(TrainingResult.user_id == user_id)
        .scalar()
    )

    correct_answers = (
        db.query(func.count(TrainingResult.id))
        .filter(
            TrainingResult.user_id == user_id,
            TrainingResult.is_correct.is_(True),
        )
        .scalar()
    )

    wrong_answers = (
        db.query(func.count(TrainingResult.id))
        .filter(
            TrainingResult.user_id == user_id,
            TrainingResult.is_correct.is_(False),
        )
        .scalar()
    )

    accuracy = 0.0
    if total_answers:
        accuracy = round((correct_answers / total_answers) * 100, 2)

    return {
        "total_answers": total_answers,
        "correct_answers": correct_answers,
        "wrong_answers": wrong_answers,
        "accuracy": accuracy,
    }


def get_hard_verbs(db: Session, user_id: int, limit: int = 5):
    results = (
        db.query(
            IrregularVerb.base_form,
            IrregularVerb.translation,
            UserProgress.correct_count,
            UserProgress.wrong_count,
        )
        .join(UserProgress, UserProgress.verb_id == IrregularVerb.id)
        .filter(UserProgress.user_id == user_id)
        .order_by(desc(UserProgress.wrong_count), UserProgress.correct_count)
        .limit(limit)
        .all()
    )

    return results