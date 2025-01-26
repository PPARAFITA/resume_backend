from pydantic import BaseModel
from typing import Optional

class UserCreate(BaseModel):
    nombre: str
    apellido: str
    email : str
    celular : int
    nacionalidad : str
    ubicacion : str

class User(BaseModel):
    userid: int
    nombre: str
    apellido: str
    email : str
    celular : int
    nacionalidad : str
    ubicacion : str

class EducationBase(BaseModel):
    school_name: str
    degree: str
    start_date : str
    end_date : str
    userid : int

class EducationCreate(EducationBase):
    pass

class EducationSchema(EducationBase):
    educationid: int

class WorkExperienceBase(BaseModel):
    company_name: str
    position: str
    start_date: str
    end_date: Optional[str] = None
    userid: int

class WorkExperienceCreate(WorkExperienceBase):
    pass

class WorkExperienceSchema(WorkExperienceBase):
    workid: int

    class Config:
        from_attributes = True