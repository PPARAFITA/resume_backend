from sqlalchemy.orm import Session
from adapters.database.workexperience_repository import WorkExperienceRepository
from core.schemas import WorkExperienceSchema, WorkExperienceCreate
from typing import List

class WorkExperienceService:
    def __init__(self, db: Session):
        self.work_repo = WorkExperienceRepository(db)

    def create_work(self, workExperience: WorkExperienceCreate) -> WorkExperienceSchema:
        return self.work_repo.create_work(workExperience)

    def get_work_by_id(self, work_id: int) -> WorkExperienceSchema:
        return self.work_repo.get_work_by_id(work_id)

    def get_works_by_user(self, user_id: int) -> List[WorkExperienceSchema]: 
        return self.work_repo.get_all_works_by_user(user_id)
