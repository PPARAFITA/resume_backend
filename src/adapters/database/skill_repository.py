from sqlalchemy.orm import Session
from core.models.skill_model import Skill
from typing import List

class SkillRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_skill(self, skill: Skill) :
        self.db.add(skill)
        self.db.commit()
        self.db.refresh(skill)
        return skill

    def update_skill(self, skill: Skill):
        try:
            self.db.commit()
            self.db.refresh(skill)
            return skill     
        except Exception as e:
            self.db.rollback()
            raise Exception(f"Error updating skill: {str(e)}")

    def get_skill_by_id(self, skill_id: int):      
        return self.db.query(Skill).filter(Skill.skillid == skill_id).first()

    def get_skills_by_user(self, userid: int):
        return( self.db.query(Skill)
               .filter(Skill.userid == userid)
               .all()
        )
