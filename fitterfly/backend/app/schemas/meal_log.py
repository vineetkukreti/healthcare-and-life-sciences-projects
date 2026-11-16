from datetime import datetime

from pydantic import BaseModel, Field


class MealItem(BaseModel):
    name: str
    portion: str
    calories: int = Field(ge=0)
    carbohydrates_g: float = Field(ge=0)
    protein_g: float = Field(ge=0)
    fat_g: float = Field(ge=0)
    fiber_g: float = Field(ge=0)


class MealEstimateRead(BaseModel):
    items: list[MealItem]
    total_calories: int
    confidence: float
    notes: str
    needs_manual_review: bool


class MealLogCreate(BaseModel):
    user_id: str = "demo-user"
    source: str = "corrected_ai"
    items: list[MealItem]
    ai_confidence: float | None = None
    confirmation_status: str = "confirmed"
    correction_history: list[dict] = Field(default_factory=list)
    notes: str | None = None


class MealLogRead(BaseModel):
    id: int
    user_id: str
    captured_at: datetime
    source: str
    items: list[MealItem]
    calories: int
    carbohydrates_g: float
    protein_g: float
    fat_g: float
    fiber_g: float
    ai_confidence: float | None
    confirmation_status: str
    correction_history: list[dict]
    notes: str | None

    model_config = {"from_attributes": True}
