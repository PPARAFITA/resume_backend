from sqlalchemy.orm import Session
from adapters.database.education_repository import EducationRepository
from core.schemas import EducationSchema, EducationCreate
from typing import List

class EducationService:
    def __init__(self, db: Session):
        self.education_repo = EducationRepository(db)

    def create_education(self, education: EducationCreate) -> EducationSchema:
        return self.education_repo.create_education(education)

    def get_education_by_id(self, education_id: int) -> EducationSchema:
        return self.education_repo.get_education_by_id(education_id)

    def get_educations_by_user(self,user_id: int) -> List[EducationSchema]: 
        return self.education_repo.get_all_educations_by_user(user_id)