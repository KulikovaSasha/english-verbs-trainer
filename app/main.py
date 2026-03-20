from fastapi import FastAPI

from app.database.db import Base, engine
from app.database import models # needed for SQLAlchemy models registration

Base.metadata.create_all(bind=engine)

app = FastAPI(title="English Verbs Trainer")


@app.get("/")
async def root():
    return {"message": "English Verbs Trainer API is running"}