from sqlalchemy.orm import Session
from core.models.skill_model import Skill
from core.schemas import SkillBase
from typing import List

class SkillRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_skill(self, skill: SkillBase) :
        new_skill = SkillBase(user_skill=skill.user_skill, userid=skill.userid )
        self.db.add(new_skill)
        self.db.commit()
        self.db.refresh(new_skill)
        return new_skill

    def update_skill(self, skill_id: int, skill: SkillBase):
        db_skill = None
        if skill_id:
            db_skill = self.get_skill_by_id(skill_id)

        if db_skill:
            db_skill.skillid    = skill.skillid
            db_skill.user_skill = skill.user_skill
            db_skill.userid     = skill.userid
            self.db.commit()
            self.db.refresh(db_skill)      

        return db_skill

    def get_skill_by_id(self, skill_id: int):
        skill_db = None
        if skill_id:
           skill_db = self.db.query(Skill).filter(Skill.skillid == skill_id).first()
        return skill_db

    def get_skills_by_user(self, userid: int):
        db_skill = None
        if userid:
            db_skill = self.db.query(Skill).filter(Skill.userid == userid).all()
        return db_skill
