import base64
import json
import re

import httpx

from app.core.config import settings
from app.services.providers import MealEstimate, MealEstimateItem, MealVisionProvider


class OllamaMealVisionProvider(MealVisionProvider):
    def __init__(
        self,
        base_url: str | None = None,
        model: str | None = None,
        timeout: float = 90.0,
    ) -> None:
        self.base_url = (base_url or settings.ollama_base_url).rstrip("/")
        self.model = model or settings.ollama_model
        self.timeout = timeout

    async def analyze_meal_bytes(
        self,
        image_bytes: bytes,
        image_name: str | None,
        content_type: str | None,
    ) -> MealEstimate:
        if content_type not in {"image/jpeg", "image/png", "image/webp"}:
            return _uncertain_estimate("Unsupported image type. Please upload a JPEG, PNG, or WebP meal photo.")

        image_base64 = base64.b64encode(image_bytes).decode("ascii")
        payload = {
            "model": self.model,
            "stream": False,
            "messages": [
                {
                    "role": "user",
                    "content": (
                        "You are helping with diabetes and obesity meal logging. "
                        "Identify visible foods and estimate portions and nutrition. "
                        "Return only valid JSON with this exact shape: "
                        '{"items":[{"name":"string","portion":"string","calories":0,'
                        '"carbohydrates_g":0,"protein_g":0,"fat_g":0,"fiber_g":0}],'
                        '"confidence":0.0,"notes":"string","needs_manual_review":false}. '
                        "Use conservative estimates. If uncertain, set needs_manual_review true."
                    ),
                    "images": [image_base64],
                }
            ],
        }

        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.post(f"{self.base_url}/api/chat", json=payload)
                response.raise_for_status()
                content = response.json()["message"]["content"]
        except (httpx.HTTPError, KeyError, TypeError, ValueError):
            return _uncertain_estimate("Local vision model is unavailable. Please enter the meal manually.")

        return _parse_ollama_estimate(content)

    async def analyze_meal(self, image_name: str | None, content_type: str | None) -> MealEstimate:
        return _uncertain_estimate("No image bytes were provided to the Ollama vision provider.")


def _parse_ollama_estimate(content: str) -> MealEstimate:
    try:
        parsed = json.loads(_extract_json(content))
        items = [
            MealEstimateItem(
                name=str(item.get("name", "Unknown food")),
                portion=str(item.get("portion", "Needs confirmation")),
                calories=max(0, int(float(item.get("calories", 0)))),
                carbohydrates_g=max(0.0, float(item.get("carbohydrates_g", 0))),
                protein_g=max(0.0, float(item.get("protein_g", 0))),
                fat_g=max(0.0, float(item.get("fat_g", 0))),
                fiber_g=max(0.0, float(item.get("fiber_g", 0))),
            )
            for item in parsed.get("items", [])
        ]
        if not items:
            return _uncertain_estimate("Vision model did not identify any food items. Please enter manually.")
        return MealEstimate(
            items=items,
            total_calories=sum(item.calories for item in items),
            confidence=max(0.0, min(1.0, float(parsed.get("confidence", 0.5)))),
            notes=str(parsed.get("notes", "Review before saving.")),
            needs_manual_review=bool(parsed.get("needs_manual_review", False)),
        )
    except (TypeError, ValueError, json.JSONDecodeError):
        return _uncertain_estimate("Vision model response could not be parsed. Please enter the meal manually.")


def _extract_json(content: str) -> str:
    content = content.strip()
    if content.startswith("```"):
        match = re.search(r"```(?:json)?\s*(.*?)\s*```", content, flags=re.DOTALL)
        if match:
            return match.group(1)
    start = content.find("{")
    end = content.rfind("}")
    if start != -1 and end != -1 and end > start:
        return content[start : end + 1]
    return content


def _uncertain_estimate(notes: str) -> MealEstimate:
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
        confidence=0.2,
        notes=notes,
        needs_manual_review=True,
    )
