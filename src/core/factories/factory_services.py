from src.core.services.user_service import UserService
from src.core.services.education_service import EducationService
from src.core.services.work_experience_service import WorkExperienceService
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.adapters.database.database import get_db

class ServiceFactory:
    def __init__(self, db: Session = Depends(get_db)):
        self.user_service = UserService(db)
        self.education_service = EducationService(db)
        self.work_experience_service = WorkExperienceService(db)

def get_service_factory(factory: ServiceFactory = Depends()):
    return factory
