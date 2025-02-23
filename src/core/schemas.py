from pydantic import BaseModel
from typing import Optional

class UserBase(BaseModel):
    nombre: str
    apellido: str
    email : str
    celular : int
    nacionalidad : str
    ubicacion : str
    github : Optional[str] = None
    linkedin : Optional[str] = None

class User(UserBase):
    userid: int


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