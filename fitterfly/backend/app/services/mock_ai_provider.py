from app.services.providers import MealEstimate, MealEstimateItem, MealVisionProvider


class MockMealVisionProvider(MealVisionProvider):
    async def analyze_meal(self, image_name: str | None, content_type: str | None) -> MealEstimate:
        name = (image_name or "").lower()
        if not image_name or "blurry" in name or content_type not in {"image/jpeg", "image/png", "image/webp"}:
            return MealEstimate(
                items=[
                    MealEstimateItem(
                        name="Unknown meal",
                        portion="Needs user confirmation",
                        calories=0,
                        carbohydrates_g=0,
                        protein_g=0,
                        fat_g=0,
                        fiber_g=0,
                    )
                ],
                total_calories=0,
                confidence=0.35,
                notes="Image could not be confidently recognized. Please enter the meal manually.",
                needs_manual_review=True,
            )

        if "idli" in name or "south" in name:
            items = [
                MealEstimateItem("Idli", "2 pieces", 156, 32, 6, 1, 2),
                MealEstimateItem("Sambar", "1 bowl", 120, 18, 6, 3, 5),
                MealEstimateItem("Coconut chutney", "2 tbsp", 90, 4, 2, 8, 1),
            ]
            notes = "Recognized a South Indian breakfast plate. Confirm chutney and portion size."
        else:
            items = [
                MealEstimateItem("Brown rice", "1 cup", 216, 45, 5, 2, 4),
                MealEstimateItem("Dal", "1 bowl", 180, 28, 11, 4, 7),
                MealEstimateItem("Mixed vegetables", "1 cup", 110, 18, 4, 3, 6),
            ]
            notes = "Mock estimate for a balanced Indian meal. Please confirm portions before saving."

        return MealEstimate(
            items=items,
            total_calories=sum(item.calories for item in items),
            confidence=0.82,
            notes=notes,
            needs_manual_review=False,
        )
