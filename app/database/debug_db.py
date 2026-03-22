from app.database.db import SessionLocal
from app.database.models import TrainingResult, UserProgress


def show_training_results():
    db = SessionLocal()

    print("\n--- TRAINING RESULTS ---")
    results = db.query(TrainingResult).all()

    for r in results:
        print(
            f"id={r.id}, user_id={r.user_id}, verb_id={r.verb_id}, "
            f"is_correct={r.is_correct}, answer={r.user_answer}"
        )

    db.close()


def show_user_progress():
    db = SessionLocal()

    print("\n--- USER PROGRESS ---")
    progress = db.query(UserProgress).all()

    for p in progress:
        print(
            f"user_id={p.user_id}, verb_id={p.verb_id}, "
            f"correct={p.correct_count}, wrong={p.wrong_count}"
        )

    db.close()


if __name__ == "__main__":
    show_training_results()
    show_user_progress()