from sqlalchemy.orm import Session

from app.models.review_case import HumanReviewCase
from app.schemas.review_case import HumanReviewCaseCreate


class ReviewService:
    def __init__(self, db: Session) -> None:
        self.db = db

    def create_case(self, payload: HumanReviewCaseCreate) -> HumanReviewCase:
        review_case = HumanReviewCase(**payload.model_dump())
        self.db.add(review_case)
        self.db.commit()
        self.db.refresh(review_case)
        return review_case
