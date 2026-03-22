import json
from pathlib import Path

from app.database.db import SessionLocal
from app.database.models import IrregularVerb



def load_verbs():
    db = SessionLocal()

    try:
        file_path = Path("data/irregular_verbs.json")

        with open(file_path, "r", encoding="utf-8") as f:
            verbs = json.load(f)

        added_count = 0

        for verb in verbs:
            exists = db.query(IrregularVerb).filter_by(
                base_form=verb["base_form"],
                past_simple=verb["past_simple"],
                past_participle=verb["past_participle"]
            ).first()

            if not exists:
                new_verb = IrregularVerb(
                    base_form=verb["base_form"],
                    past_simple=verb["past_simple"],
                    past_participle=verb["past_participle"],
                    translation=verb["translation"],
                    level=verb.get("level", "A0")
                )

                db.add(new_verb)
                added_count += 1

        db.commit()
        print(f"Added {added_count} verbs")

    finally:
        db.close()


if __name__ == "__main__":
    load_verbs()