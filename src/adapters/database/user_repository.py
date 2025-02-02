from sqlalchemy.orm import Session
from core.models import User
from core.schemas import UserCreate
from typing import List

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_user(self, user: UserCreate):
        db_user = User(nombre=user.nombre, apellido=user.apellido, email=user.email, celular=user.celular, nacionalidad = user.nacionalidad, ubicacion = user.ubicacion )
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def get_user_by_id(self, user_id: int):
        return self.db.query(User).filter(User.userid == user_id).first()

    def get_all_users(self) -> List[User]:
        return self.db.query(User)
