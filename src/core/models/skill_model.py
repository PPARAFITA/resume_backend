from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy_utils import JSONType
from .user_model import Base, User


class Skill(Base):
    __tablename__ = "skills"

    skillid = Column(Integer, primary_key=True, index=True)
    user_skill = Column(JSONType)
    userid = Column(Integer, ForeignKey('user_data.userid'))

    # Relación con otras tablas
    user = relationship("User", back_populates="skills")
    