from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.core.schemas import WorkExperienceSchema, WorkExperienceCreate
from src.core.services.work_experience_service import WorkExperienceService
from src.adapters.database.database import get_db
from typing import List

router = APIRouter()

@router.post("/works/", response_model=WorkExperienceSchema, tags=["WorkExperience"])
def create_experience(workExperience: WorkExperienceCreate, db: Session = Depends(get_db)):
    try:
        service = WorkExperienceService(db)
    except Exception as e:  
        raise HTTPException(status_code=404, detail=f"exception: {e}")  
    return service.create_work(workExperience)

@router.get("/works/{work_id}", response_model=WorkExperienceSchema, tags=["WorkExperience"])
def read_work(work_id: int, db: Session = Depends(get_db)):
    try:
        service = WorkExperienceService(db)
        db_work = service.get_work_by_id(work_id)
    except Exception as e:  
        raise HTTPException(status_code=404, detail=f"exception: {e}")  
    return db_work

@router.get("/users/{user_id}/works", response_model=List[WorkExperienceSchema], tags=["WorkExperience"])
def read_works( user_id: int, db: Session = Depends(get_db)):
    try:
        service = WorkExperienceService(db)
        works_list = service.get_works_by_user(user_id)
    except Exception as e:  
        raise HTTPException(status_code=404, detail=f"exception: {e}")  
    return works_list

@router.patch("/works/{work_id}", response_model=WorkExperienceSchema, tags=["WorkExperience"])
def update_work(work_id: int, workExperience: WorkExperienceSchema, db: Session = Depends(get_db)):
    try:
        service = WorkExperienceService(db)
        work_upd = service.update_work(work_id, workExperience )
    except Exception as e:  
        raise HTTPException(status_code=404, detail=f"exception: {e}")  
    return work_upd  
