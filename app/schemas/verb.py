from pydantic import BaseModel, ConfigDict


class VerbResponse(BaseModel):
    id: int
    base_form: str
    past_simple: str
    past_participle: str
    translation: str
    level: str

    model_config = ConfigDict(from_attributes=True)