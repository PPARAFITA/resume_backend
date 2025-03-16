from sqlalchemy.orm import Session
from core.models.education_model import Education
from typing import List

class EducationRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_education(self, education: Education) -> Education:
        try:
            self.db.add(education)
            self.db.commit()
            self.db.refresh(education)
            return education
        except Exception as e:
            self.db.rollback()
            raise Exception(f"Error creating education: {str(e)}")

    def update_education(self, education: Education) -> Education:
        try:
            self.db.commit()
            self.db.refresh(education)
            return education
        except Exception as e:
            self.db.rollback()
            raise Exception(f"Error updating education: {str(e)}")
        
    def get_education_by_id(self, education_id: int) -> Education:
        return( self.db.query(Education)
               .filter(Education.education_id == education_id)
               .first()
        )

    def get_all_educations_by_user(self, user_id: int) -> List[Education]:
        return( 
            self.db.query(Education)
            .filter(Education.userid == user_id)
            .all()
        )