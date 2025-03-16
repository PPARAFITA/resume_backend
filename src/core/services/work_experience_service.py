from sqlalchemy.orm import Session
from adapters.database.workexperience_repository import WorkExperienceRepository
from core.models.work_experience_model import WorkExperience
from core.schemas import WorkExperienceSchema, WorkExperienceCreate
from core.interfaces.work_experience_service_interf import WorkExperienceServiceInterf
from typing import List
from FastApi import HTTPException

class WorkExperienceService(WorkExperienceServiceInterf):
    def __init__(self, db: Session):
        self.work_repo = WorkExperienceRepository(db)

    def create_work(self, workExperience: WorkExperienceCreate) -> WorkExperienceSchema:
        try:
            work_model = WorkExperience(**workExperience.dict())
            created_work = self.work_repo.create_workExperience(work_model)
            return WorkExperienceSchema.from_orm(created_work)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error creating work experience: {str(e)}")

    def update_work(self, work_id: int, workExperience: WorkExperienceSchema) -> WorkExperienceSchema:
        if not work_id:   
            raise HTTPException(status_code=400, detail=f"work id is mandatory")
        
        db_work = self.work_repo.get_work_by_id(work_id) 
        if not db_work:
            raise HTTPException(status_code=404, detail=f"work id not exist: {str(e)}")
       
        try:         
            work_model = WorkExperience(**workExperience.dict())
            updated_work = self.work_repo.update_workExperience(work_model)
            return WorkExperienceSchema.from_orm(updated_work)
        except Exception as e: 
            raise HTTPException(status_code=500, detail=f"{str(e)}")

    def get_work_by_id(self, work_id: int) -> WorkExperienceSchema:
        if not work_id:   
            raise HTTPException(status_code=400, detail=f"work id is mandatory")
        
        db_work = self.work_repo.get_work_by_id(work_id)
        if not db_work:
            raise HTTPException(status_code=404, detail="Work experience not found")
        
        return WorkExperienceSchema.from_orm(db_work)

    def get_works_by_user(self, user_id: int) -> List[WorkExperienceSchema]: 
        if not user_id:
            raise HTTPException(status_code=400, detail=f"user id is mandatory")
        
        work_list = self.work_repo.get_all_works_by_user(user_id)
        if not work_list:
            raise HTTPException(status_code=404, detail="No work experiences found for the user")
        
        return [WorkExperienceSchema.from_orm(work) for work in work_list]
