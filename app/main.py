from fastapi import FastAPI

from app.api.routes import router
from app.database.db import Base, engine
from app.database import models # needed for SQLAlchemy models registration

Base.metadata.create_all(bind=engine)

app = FastAPI(title="English Verbs Trainer")

app.include_router(router)


@app.get("/")
async def root():
    return {"message": "English Verbs Trainer API is running"}