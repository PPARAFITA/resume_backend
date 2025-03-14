from sqlalchemy.orm import Session
from adapters.database.skill_repository import SkillRepository
from core.schemas import SkillBase
from core.interfaces.skill_service_interf import SkillServiceInterf
from typing import List
from fastapi import HTTPException

class SkillService(SkillServiceInterf):
    def __init__(self, db: Session):
        self.skill_repo = SkillRepository(db)

    def create_skill(self, skill: SkillBase) -> SkillBase:
        created_skill = SkillBase.model_validate(self.skill_repo.create_skill(skill))
        return created_skill

   
    def get_skill_by_id(self, skill_id: int) -> SkillBase:
        try:
            db_skill = self.skill_repo.get_skill_by_id(skill_id)
            if db_skill is None:
                raise HTTPException(status_code=404, detail="Skill not found")

            skill_data = SkillBase.model_validate(db_skill)
        except Exception as e:    
            raise HTTPException(status_code=404, detail="skills not found")
        return skill_data

    
    def get_skills_by_userid(self, userid: int) -> List[SkillBase]: 
        try:
            skills_list = self.skill_repo.get_skills_by_user(userid)
            if not skills_list:
                raise HTTPException(status_code=404, detail="skills not found")
        except Exception as e:    
            raise HTTPException(status_code=404, detail="skills not found")        
        return [SkillBase.model_validate(skill) for skill in skills_list]

    
    def update_skill(self, skill_id: int, skill: SkillBase) -> SkillBase: 
        if not skill_id:
            raise HTTPException(status_code=404, detail="Skill ID is mandatory")  

        try:    
            updated_skill_data = self.skill_repo.update_skill(skill_id, skill)
            db_skill = SkillBase.model_validate(updated_skill_data)
                
        except Exception as e:
            raise HTTPException(status_code=400, detail=f"Invalid skill data: {e}")
        
        return db_skill