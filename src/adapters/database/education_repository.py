from sqlalchemy.orm import Session
from core.models.education_model import Education
from core.schemas import EducationCreate, EducationSchema
from typing import List

class EducationRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_education(self, education: EducationCreate) -> EducationSchema:
        db_education = Education( school_name=education.school_name, degree=education.degree, start_date=education.start_date, end_date=education.end_date, userid = education.userid )
        self.db.add(db_education)
        self.db.commit()
        self.db.refresh(db_education)
        return db_education

    def get_education_by_id(self, education_id: int) -> EducationSchema:
        db_education = self.db.query(Education).filter(Education.education_id == education_id).first()
        if not db_education:
            raise HTTPException(status_code=404, detail="User not found")

        return db_education

    def get_all_educations_by_user(self, user_id: int) -> List[EducationSchema]:
        db_education_list = self.db.query(Education).filter(Education.userid == user_id)
        if not db_education_list:
            raise HTTPException(status_code=404, detail="Educations not found")
        return db_education_list 