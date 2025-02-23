from sqlalchemy.orm import Session
from adapters.database.user_repository import UserRepository
from core.schemas import UserBase, User
from typing import List

class UserService:
    def __init__(self, db: Session):
        self.user_repo = UserRepository(db)

    def create_user(self, user: UserBase) -> User:
        return self.user_repo.create_user(user)

    def get_user_by_id(self, user_id: int) -> User:
        return self.user_repo.get_user_by_id(user_id)

    def get_users(self) -> List[User]: 
        return self.user_repo.get_all_users()

    def update_user(self, user_id: int, user: UserBase) -> User: 
        return self.user_repo.update_user(user_id, user)