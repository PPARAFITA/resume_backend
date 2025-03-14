from sqlalchemy.orm import Session
from adapters.database.user_repository import UserRepository
from core.interfaces.user_service_interf import UserServiceInterf
from core.schemas import UserBase, User as UserSchema
from typing import List, Dict, Optional
import json

class UserService(UserServiceInterf):
    def __init__(self, db: Session):
        self.user_repo = UserRepository(db)

    def create_user(self, user: UserBase) -> UserSchema:
        created_user = UserSchema.from_orm(self.user_repo.create_user(user))
        return created_user

    def get_user_by_id(self, user_id: int) -> Optional[UserSchema]:
        db_user = self.user_repo.get_user_by_id(user_id)
        if db_user:
            return UserSchema.from_orm(db_user)
        return None

    def get_users(self) -> List[UserSchema]:
        users_list = self.user_repo.get_all_users()
        return [UserSchema.from_orm(user) for user in users_list]

    def update_user(self, user_id: int, user: UserBase) -> UserSchema:
        updated_user = UserSchema.from_orm(self.user_repo.update_user(user_id, user))
        return updated_user