from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.meal_log import MealLog
from app.schemas.meal_log import MealLogCreate
from app.services.audit_service import AuditService


class MealLogService:
    def __init__(self, db: Session, audit_service: AuditService | None = None) -> None:
        self.db = db
        self.audit_service = audit_service or AuditService()

    def create(self, payload: MealLogCreate) -> MealLog:
        totals = self._totals(payload)
        meal_log = MealLog(
            user_id=payload.user_id,
            source=payload.source,
            items=[item.model_dump() for item in payload.items],
            calories=totals["calories"],
            carbohydrates_g=totals["carbohydrates_g"],
            protein_g=totals["protein_g"],
            fat_g=totals["fat_g"],
            fiber_g=totals["fiber_g"],
            ai_confidence=payload.ai_confidence,
            confirmation_status=payload.confirmation_status,
            correction_history=payload.correction_history,
            notes=payload.notes,
        )
        self.db.add(meal_log)
        self.db.commit()
        self.db.refresh(meal_log)
        self.audit_service.record(
            "meal_log.created",
            "meal_log",
            meal_log.id,
            {"user_id": meal_log.user_id, "confirmation_status": meal_log.confirmation_status},
        )
        return meal_log

    def list_for_user(self, user_id: str) -> list[MealLog]:
        statement = select(MealLog).where(MealLog.user_id == user_id).order_by(MealLog.captured_at.desc())
        return list(self.db.scalars(statement).all())

    @staticmethod
    def _totals(payload: MealLogCreate) -> dict[str, float | int]:
        return {
            "calories": sum(item.calories for item in payload.items),
            "carbohydrates_g": sum(item.carbohydrates_g for item in payload.items),
            "protein_g": sum(item.protein_g for item in payload.items),
            "fat_g": sum(item.fat_g for item in payload.items),
            "fiber_g": sum(item.fiber_g for item in payload.items),
        }
