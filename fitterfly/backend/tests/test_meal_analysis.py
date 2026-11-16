import pytest

from app.services.meal_analysis_service import MealAnalysisService


@pytest.mark.anyio
async def test_meal_analysis_returns_editable_estimate():
    estimate = await MealAnalysisService().analyze("south-indian-idli.png", "image/png")

    assert estimate.confidence > 0.8
    assert estimate.needs_manual_review is False
    assert estimate.total_calories == sum(item.calories for item in estimate.items)
    assert estimate.items[0].name == "Idli"


@pytest.mark.anyio
async def test_meal_analysis_flags_uncertain_images():
    estimate = await MealAnalysisService().analyze("blurry-photo.txt", "text/plain")

    assert estimate.needs_manual_review is True
    assert estimate.confidence < 0.5
    assert "manually" in estimate.notes.lower()
