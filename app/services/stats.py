from sqlalchemy.orm import Session

from app.crud.progress import get_hard_verbs, get_user_training_stats


def get_user_stats(db: Session, user_id: int):
    stats = get_user_training_stats(db, user_id)
    hard_verbs_raw = get_hard_verbs(db, user_id)

    hard_verbs = [
        {
            "base_form": verb.base_form,
            "translation": verb.translation,
            "correct_count": verb.correct_count,
            "wrong_count": verb.wrong_count,
        }
        for verb in hard_verbs_raw
    ]

    return {
        "total_answers": stats["total_answers"],
        "correct_answers": stats["correct_answers"],
        "wrong_answers": stats["wrong_answers"],
        "accuracy": stats["accuracy"],
        "hard_verbs": hard_verbs,
    }
