from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.core.schemas import SkillBase
from src.core.services.skill_service import SkillService
from src.adapters.database.database import get_db
from typing import List

router = APIRouter()

@router.post("/skill/", response_model=SkillBase, tags=["Skills"])
def create_skill(skill: SkillBase, db: Session = Depends(get_db)):
    service = SkillService(db)
    return service.create_skill(skill)

@router.get("/skill/{skill_id}", response_model=SkillBase, tags=["Skills"])
def read_skill(skill_id: int, db: Session = Depends(get_db)):
    try:
        service = SkillService(db)
        db_skill = service.get_skill_by_id(skill_id)
    except Exception as e:  
        raise HTTPException(status_code=404, detail=f"exception: {e}")   
    return db_skill

@router.get("/skill/{user_id}/skills", response_model=List[SkillBase], tags=["Skills"])
def read_skills( user_id: int, db: Session = Depends(get_db)):
    try: 
        service = SkillService(db)
        skills_list = service.get_skills_by_userid(user_id)
    except Exception as e:  
        raise HTTPException(status_code=404, detail=f"exception: {e}")
    return skills_list

@router.patch("/skill/{skill_id}", response_model=SkillBase, tags=["Skills"])
def update_skill(skill_id: int, skill: SkillBase, db: Session = Depends(get_db)):
    try:
        service = SkillService(db)
        skill_upd = service.update_skill(skill_id, skill )
    except Exception as e: 
        raise HTTPException(status_code=404, detail=f"exception: {e}")
    return skill_upd  
