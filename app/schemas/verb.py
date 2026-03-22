from pydantic import BaseModel, ConfigDict


class VerbResponse(BaseModel):
    id: int
    base_form: str
    past_simple: str
    past_participle: str
    translation: str
    level: str

    model_config = ConfigDict(from_attributes=True)

class TrainingTaskResponse(BaseModel):
    verb_id: int
    base_form: str
    translation: str
    level: str

    model_config = ConfigDict(from_attributes=True)


class TrainingAnswerRequest(BaseModel):
    user_id: int
    verb_id: int
    past_simple: str
    past_participle: str


class TrainingCheckResponse(BaseModel):
    is_correct: bool
    correct_past_simple: str
    correct_past_participle: str
    message: str