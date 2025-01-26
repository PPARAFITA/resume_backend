from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "user_data"

    userid = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    apellido = Column(String, index=True)
    email = Column(String)
    celular = Column(Integer)
    nacionalidad = Column(String)
    ubicacion = Column(String)

# Relación con WorkExperience
    work_experiences = relationship("WorkExperience", back_populates="user")
    education - relationship("Education", back_populates="user")

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
