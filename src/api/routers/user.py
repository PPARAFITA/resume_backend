from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from core.schemas import User, UserBase
from core.services.user_service import UserService
from database import get_db
from typing import List

router = APIRouter()

@router.post("/users/", response_model=User, tags=["User"])
def create_user(user: UserBase, db: Session = Depends(get_db)):
    service = UserService(db)
    return service.create_user(user)

@router.get("/users/{user_id}", response_model=User, tags=["User"])
def read_user(user_id: int, db: Session = Depends(get_db)):
    service = UserService(db)
    db_user = service.get_user_by_id(user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.get("/users", response_model=List[User], tags=["User"])
def read_users( db: Session = Depends(get_db)):
    service = UserService(db)
    users_list = service.get_users()
    if users_list is None:
        raise HTTPException(status_code=404, detail="User not found")
    return users_list

@router.patch("/users/{user_id}", response_model=User, tags=["User"])
def update_user(user_id: int, user: UserBase, db: Session = Depends(get_db)):
    service = UserService(db)
    user_updated = service.update_user(user_id, user)
    if user_updated is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user_updated    
