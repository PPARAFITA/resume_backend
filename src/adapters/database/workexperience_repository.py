from sqlalchemy.orm import Session
from core.models.work_experience_model import WorkExperience
from core.schemas import WorkExperienceCreate, WorkExperienceSchema
from typing import List

class WorkExperienceRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_workExperience(self, experience: WorkExperienceCreate) -> WorkExperience:
        db_work_experience = WorkExperience(company_name=experience.company_name, position=experience.position, start_date=experience.start_date, end_date=experience.end_date, userid = experience.userid )
        self.db.add(db_work_experience)
        self.db.commit()
        self.db.refresh(db_work_experience)
        return db_work_experience

    def get_work_by_id(self, workexperience_id: int) -> WorkExperience:
        return self.db.query(WorkExperience).filter(WorkExperience.workid == workexperience_id).first()

    def get_all_works_by_user(self, userid: int) -> List[WorkExperience]:
        return self.db.query(WorkExperience).filter(WorkExperience.userid == userid)
