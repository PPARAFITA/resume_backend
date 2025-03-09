from sqlalchemy.orm import Session
from adapters.database.workexperience_repository import WorkExperienceRepository
from core.schemas import WorkExperienceSchema, WorkExperienceCreate
from core.interfaces.work_experience_service_interf import WorkExperienceServiceInterf
from typing import List

class WorkExperienceService(WorkExperienceServiceInterf):
    def __init__(self, db: Session):
        self.work_repo = WorkExperienceRepository(db)

    def create_work(self, workExperience: WorkExperienceCreate) -> WorkExperienceSchema:
        return WorkExperienceSchema.from_orm(self.work_repo.create_workExperience(workExperience))

    def update_work(self, work_id: int, workExperience: WorkExperienceSchema) -> WorkExperienceSchema:
        return WorkExperienceSchema.from_orm(self.work_repo.update_workExperience(work_id, workExperience))

    def get_work_by_id(self, work_id: int) -> WorkExperienceSchema:
        return WorkExperienceSchema.from_orm(self.work_repo.get_work_by_id(work_id))

    def get_works_by_user(self, user_id: int) -> List[WorkExperienceSchema]: 
        work_list = self.work_repo.get_all_works_by_user(user_id)
        return[WorkExperienceSchema.from_orm(work) for work in work_list]  
