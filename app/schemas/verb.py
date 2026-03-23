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
    points_earned: int
    total_score: int

class HardVerbResponse(BaseModel):
    base_form: str
    translation: str
    correct_count: int
    wrong_count: int


class UserStatsResponse(BaseModel):
    total_answers: int
    correct_answers: int
    wrong_answers: int
    accuracy: float
    hard_verbs: list[HardVerbResponse]

class LevelProgressResponse(BaseModel):
    level: str
    total_verbs: int
    learned_verbs: int
    progress_percent: float