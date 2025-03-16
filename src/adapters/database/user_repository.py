from sqlalchemy.orm import Session
from core.models.user_model import User
from typing import Optional, List

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_user_by_id(self, user_id: int) -> Optional[User]:
        return self.db.query(User).filter(User.userid == user_id).first()

    def get_all_users(self) -> List[User]:
        return self.db.query(User).all()

    def create_user(self, user: User) -> User:
        try:
            self.db.add(user)
            self.db.commit()
            self.db.refresh(user)
            return user
        except Exception as e:
            self.db.rollback()
            raise Exception(f"Error creating user: {str(e)}")

    def update_user(self, user: User) -> User:
        try:
            self.db.commit()
            self.db.refresh(user)
            return user
        except Exception as e:
            self.db.rollback()
            raise Exception(f"Error updating user: {str(e)}")