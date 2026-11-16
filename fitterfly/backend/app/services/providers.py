from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass(frozen=True)
class MealEstimateItem:
    name: str
    portion: str
    calories: int
    carbohydrates_g: float
    protein_g: float
    fat_g: float
    fiber_g: float


@dataclass(frozen=True)
class MealEstimate:
    items: list[MealEstimateItem]
    total_calories: int
    confidence: float
    notes: str
    needs_manual_review: bool


class MealVisionProvider(ABC):
    @abstractmethod
    async def analyze_meal(self, image_name: str | None, content_type: str | None) -> MealEstimate:
        """Return an editable nutrition estimate for a meal photo."""
