from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

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
    github = Column(String, nullable=True)  
    linkedin = Column(String, nullable=True) 

    # Relación con otras tablas
    work_experiences = relationship("WorkExperience", back_populates="user")
    education = relationship("Education", back_populates="user")