from sqlalchemy.orm import Session

from app.database.models import IrregularVerb, TrainingResult, UserProgress


def get_training_task(db: Session):
    verb = db.query(IrregularVerb).order_by(IrregularVerb.id).first()

    if verb is None:
        return None

    return {
        "verb_id": verb.id,
        "base_form": verb.base_form,
        "translation": verb.translation,
        "level": verb.level,
    }


def check_training_answer(
    db: Session,
    user_id: int,
    verb_id: int,
    past_simple: str,
    past_participle: str,
):
    verb = db.query(IrregularVerb).filter(IrregularVerb.id == verb_id).first()

    if verb is None:
        return None

    normalized_past_simple = past_simple.strip().lower()
    normalized_past_participle = past_participle.strip().lower()

    correct_past_simple = verb.past_simple.strip().lower()
    correct_past_participle = verb.past_participle.strip().lower()

    is_correct = (
        normalized_past_simple == correct_past_simple
        and normalized_past_participle == correct_past_participle
    )

    result = TrainingResult(
        user_id=user_id,
        verb_id=verb.id,
        user_answer=f"{past_simple} | {past_participle}",
        correct_answer=f"{verb.past_simple} | {verb.past_participle}",
        is_correct=is_correct,
    )
    db.add(result)

    progress = (
        db.query(UserProgress)
        .filter(
            UserProgress.user_id == user_id,
            UserProgress.verb_id == verb.id,
        )
        .first()
    )

    if progress is None:
        progress = UserProgress(
            user_id=user_id,
            verb_id=verb.id,
            correct_count=0,
            wrong_count=0,
        )
        db.add(progress)

    if is_correct:
        progress.correct_count += 1
        message = "Correct!"
    else:
        progress.wrong_count += 1
        message = "Incorrect."

    db.commit()

    return {
        "is_correct": is_correct,
        "correct_past_simple": verb.past_simple,
        "correct_past_participle": verb.past_participle,
        "message": message,
    }