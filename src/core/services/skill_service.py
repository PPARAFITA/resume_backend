from sqlalchemy.orm import Session
from adapters.database.skill_repository import SkillRepository
from core.schemas import SkillBase
from core.models.skill_model import Skill
from core.interfaces.skill_service_interf import SkillServiceInterf
from typing import List
from fastapi import HTTPException

class SkillService(SkillServiceInterf):
    def __init__(self, db: Session):
        self.skill_repo = SkillRepository(db)

    def create_skill(self, skill: SkillBase) -> SkillBase:
        skill_model = Skill(**skill.dict())
        try:   
            created_skill = self.skill_repo.create_skill(skill_model)
            return SkillBase.from_orm(created_skill)
        except Exception as e:
            raise HTTPException(status_code=400, detail=f"Error creating skill:{str(e)}")

   
    def get_skill_by_id(self, skill_id: int) -> SkillBase:
        if not skill_id:
            raise HTTPException(status_code=400, detail="the skill ID is mandatory") 

        db_skill = self.skill_repo.get_skill_by_id(skill_id)
        if not db_skill:
            raise HTTPException(status_code=404, detail="Skill not found")

        return SkillBase.from_orm(db_skill)

    
    def get_skills_by_userid(self, userid: int) -> List[SkillBase]: 
        if not userid:
            raise HTTPException(status_code=400, detail="the user ID is mandatory") 
        
        skills_list = self.skill_repo.get_skills_by_user(userid)
        if not skills_list:
            raise HTTPException(status_code=404, detail="skills not found")
        
        return [SkillBase.from_orm(skill) for skill in skills_list]  
        
    
    def update_skill(self, skill_id: int, skill: SkillBase) -> SkillBase: 
        if not skill_id:
            raise HTTPException(status_code=404, detail="Skill ID is mandatory")  
        
        db_skill = self.get_skill_by_id(skill_id)
        
        try:
            skill_model = Skill(**skill.dict())    
            updated_skill_data = self.skill_repo.update_skill(skill_model)
            return SkillBase.from_orm(updated_skill_data)
        except Exception as e:
            raise HTTPException(status_code=400, detail=f"{e}")
    