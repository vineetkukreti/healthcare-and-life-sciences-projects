from app.schemas.meal_log import MealEstimateRead, MealItem
from app.core.config import settings
from app.services.mock_ai_provider import MockMealVisionProvider
from app.services.ollama_vision_provider import OllamaMealVisionProvider
from app.services.providers import MealVisionProvider


class MealAnalysisService:
    def __init__(self, provider: MealVisionProvider | None = None) -> None:
        self.provider = provider or MockMealVisionProvider()

    async def analyze(self, image_name: str | None, content_type: str | None) -> MealEstimateRead:
        estimate = await self.provider.analyze_meal(image_name=image_name, content_type=content_type)
        return self._to_schema(estimate)

    async def analyze_bytes(
        self,
        image_bytes: bytes,
        image_name: str | None,
        content_type: str | None,
    ) -> MealEstimateRead:
        if isinstance(self.provider, OllamaMealVisionProvider):
            estimate = await self.provider.analyze_meal_bytes(image_bytes, image_name, content_type)
        else:
            estimate = await self.provider.analyze_meal(image_name=image_name, content_type=content_type)
        return self._to_schema(estimate)

    @staticmethod
    def _to_schema(estimate):
        return MealEstimateRead(
            items=[
                MealItem(
                    name=item.name,
                    portion=item.portion,
                    calories=item.calories,
                    carbohydrates_g=item.carbohydrates_g,
                    protein_g=item.protein_g,
                    fat_g=item.fat_g,
                    fiber_g=item.fiber_g,
                )
                for item in estimate.items
            ],
            total_calories=estimate.total_calories,
            confidence=estimate.confidence,
            notes=estimate.notes,
            needs_manual_review=estimate.needs_manual_review,
        )


def get_meal_analysis_service() -> MealAnalysisService:
    if settings.meal_vision_provider.lower() == "ollama":
        return MealAnalysisService(OllamaMealVisionProvider())
    return MealAnalysisService(MockMealVisionProvider())
