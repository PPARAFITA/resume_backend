from sqlalchemy.orm import Session
from core.models.work_experience_model import WorkExperience
from core.schemas import WorkExperienceCreate, WorkExperienceSchema
from typing import List

class WorkExperienceRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_workExperience(self, experience: WorkExperienceCreate) :
        db_work_experience = WorkExperience(company_name=experience.company_name, position=experience.position, start_date=experience.start_date, end_date=experience.end_date, userid = experience.userid, description = experience.description  )
        self.db.add(db_work_experience)
        self.db.commit()
        self.db.refresh(db_work_experience)
        return db_work_experience

    def update_workExperience(self, work_id: int, experience: WorkExperienceSchema):
        db_work_experience = self.get_work_by_id(work_id)
        
        if not db_work_experience:
            raise HTTPException(status_code=404, detail="work experience not found")

        db_work_experience.company_name = experience.company_name, 
        db_work_experience.position = experience.position, 
        db_work_experience.description = experience.description
        db_work_experience.start_date = experience.start_date, 
        db_work_experience.end_date = experience.end_date, 
        db_work_experience.description = experience.description, 
        db_work_experience.userid = experience.userid

        self.db.commit()
        self.db.refresh(db_work_experience)
        return db_work_experience

    def get_work_by_id(self, workexperience_id: int):
        db_work_experience = self.db.query(WorkExperience).filter(WorkExperience.workid == workexperience_id).first()
        return db_work_experience 

    def get_all_works_by_user(self, userid: int):
        db_work_list = self.db.query(WorkExperience).filter(WorkExperience.userid == userid).order_by(WorkExperience.start_date.desc()).all()
        return db_work_list
