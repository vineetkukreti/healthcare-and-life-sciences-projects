from datetime import datetime

from pydantic import BaseModel


class HumanReviewCaseCreate(BaseModel):
    user_id: str
    source_type: str
    source_id: str | None = None
    reason: str
    assigned_role: str = "coach"


class HumanReviewCaseRead(HumanReviewCaseCreate):
    id: int
    status: str
    resolution_notes: str | None = None
    created_at: datetime
    resolved_at: datetime | None = None

    model_config = {"from_attributes": True}
