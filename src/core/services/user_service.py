from sqlalchemy.orm import Session
from adapters.database.user_repository import UserRepository
from core.interfaces.user_service_interf import UserServiceInterf
from core.schemas import UserBase, User as UserSchema
from core.models.user_model import User as UserModel
from typing import List, Optional
from fastapi import HTTPException


class UserService(UserServiceInterf):
    def __init__(self, db: Session):
        self.user_repo = UserRepository(db)

    def create_user(self, user: UserBase) -> UserSchema:
        try:
            model_user = UserModel(**user.dict())
            created_user = self.user_repo.create_user(model_user)
            return UserSchema.from_orm(created_user)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error creating user: {str(e)}")

    def get_user_by_id(self, user_id: int) -> UserSchema:
        if not user_id:
            raise HTTPException(status_code=400, detail=f"User ID is mandatory")
        
        db_user = self.user_repo.get_user_by_id(user_id)
        if not db_user:
            raise HTTPException(status_code=404, detail=f"User not found")
        return UserSchema.from_orm(db_user)

    def get_users(self) -> List[UserSchema]:
        users_list = self.user_repo.get_all_users()
        if not users_list:
            raise HTTPException(status_code=404, detail=f"No users were found")
        return [UserSchema.from_orm(user) for user in users_list]

    def update_user(self, user_id: int, user: UserBase) -> UserSchema:
        self.get_user_by_id(user_id)
        model_user = UserModel(**user.dict())
        updated_user = self.user_repo.update_user(model_user)
        
        return UserSchema.from_orm(updated_user)