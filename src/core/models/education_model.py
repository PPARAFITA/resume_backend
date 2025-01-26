from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from .user_model import Base, User

class Education(Base):
    __tablename__ = "education"

    educationid = Column(Integer, primary_key=True, index=True)
    school_name = Column(String, index=True)
    degree = Column(String)
    start_date = Column(String)
    end_date = Column(String)
    userid = Column(Integer, ForeignKey('user_data.userid'))

    # Relación inversa con User
    user = relationship("User", back_populates="education")