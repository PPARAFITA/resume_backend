from sqlalchemy.orm import Session
from core.models.work_experience_model import WorkExperience
from typing import Optional, List

class WorkExperienceRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_workExperience(self, experience: WorkExperience)-> WorkExperience:
        try:
            self.db.add(experience)
            self.db.commit()
            self.db.refresh(experience)
            return experience
        except Exception as e:
            self.db.rollback()
            raise Exception(f"Error creating experience: {str(e)}")
        
    def update_workExperience(self, experience: WorkExperience) -> WorkExperience:
        try:
            self.db.commit()
            self.db.refresh(experience)
            return experience
        except Exception as e:
            self.db.rollback()
            raise Exception(f"Error updating experience: {str(e)}")

    def get_work_by_id(self, workexperience_id: int) -> Optional[WorkExperience]:
        return(
            self.db.query(WorkExperience)
            .filter(WorkExperience.workid == workexperience_id)
            .first() 
        )

    def get_all_works_by_user(self, userid: int) -> Optional[List[WorkExperience]]:
        return (
            self.db.query(WorkExperience)
            .filter(WorkExperience.userid == userid)
            .order_by(WorkExperience.start_date.desc())
            .all()
        )