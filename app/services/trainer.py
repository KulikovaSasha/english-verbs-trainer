from sqlalchemy.orm import Session

from app.crud.verb import get_random_verb, get_random_verb_by_level
from app.database.models import IrregularVerb, TrainingResult, User, UserProgress


def normalize_text(text: str) -> str:
    return text.strip().lower()


def parse_answer_variants(value: str) -> set[str]:
    return {
        normalize_text(part)
        for part in value.split("/")
        if normalize_text(part)
    }


def get_training_task(db: Session, level: str | None = None):
    if level:
        verb = get_random_verb_by_level(db, level)
    else:
        verb = get_random_verb(db)

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
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        return None

    verb = db.query(IrregularVerb).filter(IrregularVerb.id == verb_id).first()
    if verb is None:
        return None

    normalized_past_simple = normalize_text(past_simple)
    normalized_past_participle = normalize_text(past_participle)

    valid_past_simple_answers = parse_answer_variants(verb.past_simple)
    valid_past_participle_answers = parse_answer_variants(verb.past_participle)

    is_correct = (
        normalized_past_simple in valid_past_simple_answers
        and normalized_past_participle in valid_past_participle_answers
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

    points_earned = 0

    if is_correct:
        progress.correct_count += 1
        user.score += 10
        points_earned = 10
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
        "points_earned": points_earned,
        "total_score": user.score,
    }