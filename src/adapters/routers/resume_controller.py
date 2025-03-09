from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.core.factories.factory_services import ServiceFactory, get_service_factory
from src.core.services.user_service import UserService
from src.core.services.education_service import EducationService
from src.core.services.work_experience_service import WorkExperienceService
from src.application.show_cv_use_case import ShowCV
from src.adapters.database.database import get_db
from src.core.schemas import CV

router = APIRouter()

@router.get("/resumecv/{user_id}", response_model=CV, tags=["Resume"])
def get_resume_cv( 
    user_id: int,
    db: Session = Depends(get_db), 
    factory: ServiceFactory = Depends(get_service_factory) 
):
    show_cv_case = ShowCV( education_service = factory.education_service, user_service = factory.user_service, work_experience_service = factory.work_experience_service)
    return show_cv_case.get_resume_cv(user_id)

