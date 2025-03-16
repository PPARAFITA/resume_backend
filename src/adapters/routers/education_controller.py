from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.core.schemas import EducationCreate, EducationSchema
from src.core.services.education_service import EducationService
from adapters.database.database import get_db
from typing import List

router = APIRouter()

@router.post("/educations/", response_model=EducationSchema, tags=["Education"])
def create_education(education: EducationCreate, db: Session = Depends(get_db)):
    try:
        service = EducationService(db)
    except Exception as e:  
        raise HTTPException(status_code=404, detail=f"exception: {e}")
    return service.create_education(education)

@router.get("/educations/{education_id}", response_model=EducationSchema, tags=["Education"])
def read_education_by_id(education_id: int, db: Session = Depends(get_db)):
    try:
        service = EducationService(db)
        db_work = service.get_education_by_id(education_id)
    except Exception as e:  
        raise HTTPException(status_code=404, detail=f"exception: {e}")
    return db_work

@router.get("/users/{user_id}/educations", response_model=List[EducationSchema], tags=["Education"])
def read_educations_by_user( user_id: int, db: Session = Depends(get_db)):
    try:
        service = EducationService(db)
        education_list = service.get_educations_by_user(user_id)
    except Exception as e:  
        raise HTTPException(status_code=404, detail=f"exception: {e}")
    return education_list
