from sqlalchemy.orm import Session
from core.models import User
from core.schemas import UserBase
from typing import List

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_user(self, user: UserBase):
        db_user = User(nombre=user.nombre, apellido=user.apellido, email=user.email, celular=user.celular, nacionalidad = user.nacionalidad, ubicacion = user.ubicacion, github = user.github, linkedin = user.linkedin )
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def get_user_by_id(self, user_id: int):
        return self.db.query(User).filter(User.userid == user_id).first()

    def get_all_users(self) -> List[User]:
        return self.db.query(User)

    def update_user(self, user_id: int, user: UserBase) -> User:
        db_user = self.get_user_by_id(user_id)
        if not db_user:
            return None  # O podrías lanzar una excepción HTTP 404

        # Actualizar los campos con los nuevos valores
        db_user.nombre = user.nombre
        db_user.apellido = user.apellido
        db_user.email = user.email
        db_user.celular = user.celular
        db_user.nacionalidad = user.nacionalidad
        db_user.ubicacion = user.ubicacion
        db_user.github = user.github
        db_user.linkedin = user.linkedin

        self.db.commit()
        self.db.refresh(db_user)
        return db_user  
