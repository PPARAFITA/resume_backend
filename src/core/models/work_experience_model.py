from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from .user_model import Base, User


class WorkExperience(Base):
    __tablename__ = "work_experience"

    workid = Column(Integer, primary_key=True, index=True)
    company_name = Column(String, index=True)
    position = Column(String)
    start_date = Column(String)
    end_date = Column(String)
    userid = Column(Integer, ForeignKey('user_data.userid'))

    # Relación inversa con User
    user = relationship("User", back_populates="work_experiences")