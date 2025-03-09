from sqlalchemy.orm import Session
from adapters.database.user_repository import UserRepository
from core.interfaces.user_service_interf import UserServiceInterf
from core.schemas import UserBase, User as UserSchema
from typing import List

class UserService(UserServiceInterf):
    def __init__(self, db: Session):
        self.user_repo = UserRepository(db)

    def create_user(self, user: UserBase) -> UserSchema:
        return UserSchema.from_orm(self.user_repo.create_user(user))

    def get_user_by_id(self, user_id: int) -> UserSchema:
        return UserSchema.from_orm(self.user_repo.get_user_by_id(user_id))

    def get_users(self) -> List[UserSchema]: 
        users_list = self.user_repo.get_all_users()
        return [UserSchema.from_orm(user) for user in users_list]  

    def update_user(self, user_id: int, user: UserBase) -> UserSchema: 
        return UserSchema.from_orm(self.user_repo.update_user(user_id, user))