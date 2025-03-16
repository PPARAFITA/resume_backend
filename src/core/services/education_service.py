from sqlalchemy.orm import Session
from adapters.database.education_repository import EducationRepository
from core.schemas import EducationSchema, EducationCreate
from core.interfaces.education_service_interf import EducationServiceInterf
from core.models.education_model import Education
from typing import List
from fastapi import HTTPException

class EducationService(EducationServiceInterf):
    def __init__(self, db: Session):
        self.education_repo = EducationRepository(db)

    def create_education(self, education: EducationCreate) -> EducationSchema:
        try:
            education_model = Education(**education.dict())
            created_education = self.education_repo.create_education(education_model)
            return EducationSchema.from_orm(created_education)
        except Exception as e:
            raise HTTPException(status_code=400, detail=f"Error creating education:{str(e)}")
    
    def get_education_by_id(self, education_id: int) -> EducationSchema:
        if not education_id:
            raise HTTPException(status_code=400, detail="Education ID is mandatory")
        
        db_education = self.education_repo.get_education_by_id(education_id)
        if not db_education:
            raise HTTPException(status_code=404, detail="Education not found")
        
        return EducationSchema.from_orm(db_education)

    def get_educations_by_user(self,user_id: int) -> List[EducationSchema]: 
        if not user_id:
            raise HTTPException(status_code=400, detail="User ID is mandatory")
        
        education_list = self.education_repo.get_all_educations_by_user(user_id)
        if not education_list:
            raise HTTPException(status_code=404, detail="No educations were found")
        return [EducationSchema.from_orm(education) for education in education_list]