from sqlalchemy.orm import Session
from core.models import User
from core.schemas import UserBase, User as UserSchema
from typing import List

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_user(self, user: UserBase):
        db_user = User(nombre=user.nombre, apellido=user.apellido, email=user.email, celular=user.celular, nacionalidad = user.nacionalidad, ubicacion = user.ubicacion, github = user.github, linkedin = user.linkedin, about_me = user.about_me )
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def get_user_by_id(self, user_id: int):
        db_user = self.db.query(User).filter(User.userid == user_id).first()
        return db_user

    def get_all_users(self) -> List[UserSchema]:
        users = self.db.query(User).all()  
        return users

    def update_user(self, user_id: int, user: UserBase):
        db_user = self.get_user_by_id(user_id)
        if not db_user:
            raise HTTPException(status_code=404, detail="User not found")

        db_user.nombre = user.nombre
        db_user.apellido = user.apellido
        db_user.email = user.email
        db_user.celular = user.celular
        db_user.nacionalidad = user.nacionalidad
        db_user.ubicacion = user.ubicacion
        db_user.github = user.github
        db_user.linkedin = user.linkedin
        db_user.about_me = user.about_me

        self.db.commit()
        self.db.refresh(db_user)
        return db_user
