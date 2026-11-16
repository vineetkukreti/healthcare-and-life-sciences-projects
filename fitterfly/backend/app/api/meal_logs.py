from fastapi import APIRouter, Depends, File, Query, UploadFile
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.meal_log import MealEstimateRead, MealLogCreate, MealLogRead
from app.services.meal_analysis_service import get_meal_analysis_service
from app.services.meal_log_service import MealLogService

router = APIRouter(prefix="/meal-logs", tags=["meal logs"])


@router.post("/analyze", response_model=MealEstimateRead)
async def analyze_meal_photo(image: UploadFile = File(...)) -> MealEstimateRead:
    return await get_meal_analysis_service().analyze_bytes(
        image_bytes=await image.read(),
        image_name=image.filename,
        content_type=image.content_type,
    )


@router.post("", response_model=MealLogRead, status_code=201)
def create_meal_log(payload: MealLogCreate, db: Session = Depends(get_db)) -> MealLogRead:
    return MealLogService(db).create(payload)


@router.get("", response_model=list[MealLogRead])
def list_meal_logs(
    user_id: str = Query(default="demo-user"),
    db: Session = Depends(get_db),
) -> list[MealLogRead]:
    return MealLogService(db).list_for_user(user_id)
