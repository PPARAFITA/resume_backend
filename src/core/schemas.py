from pydantic import BaseModel, validator
from typing import Optional
from datetime import date
from src.utils.utils import parse_date 
from typing import List


class UserBase(BaseModel):
    nombre: str
    apellido: str
    email : str
    celular : int
    nacionalidad : str
    ubicacion : str
    github : Optional[str] = None
    linkedin : Optional[str] = None

    class Config:
        from_attributes = True

class User(UserBase):
    userid: int


class EducationBase(BaseModel):
    school_name: str
    degree: str
    start_date : date
    end_date : Optional[date] = None 
    userid : int

   # Validación para las fechas de inicio y fin
    @validator('start_date', 'end_date', pre=True)
    def validate_dates(cls, value):
        if value:
            # Si la fecha es una cadena, la parseamos
            if isinstance(value, str):
                return parse_date(value)
            return value  # Si ya es un objeto `datetime.date`, lo dejamos tal cual
        return value
    
    class Config:
        from_attributes = True 

class EducationCreate(EducationBase):
    pass

class EducationSchema(EducationBase):
    educationid: int

class WorkExperienceBase(BaseModel):
    company_name: str
    position: str
    start_date: date 
    end_date: Optional[date] = None 
    userid: int
    description: str
    

    # Validación para las fechas de inicio y fin
    @validator('start_date', 'end_date', pre=True)
    def validate_dates(cls, value):
        if value:
            # Si la fecha es una cadena, la parseamos
            if isinstance(value, str):
                return parse_date(value)
            return value  # Si ya es un objeto `datetime.date`, lo dejamos tal cual
        return value

class WorkExperienceCreate(WorkExperienceBase):
    pass

class WorkExperienceSchema(WorkExperienceBase):
    workid: int
    @property
    def start_date_str(self):
        return self.start_date.strftime("%Y-%m-%d") if self.start_date else None

    @property
    def end_date_str(self):
        return self.end_date.strftime("%Y-%m-%d") if self.end_date else None

    class Config:
        from_attributes = True

class CV(User, BaseModel):
    work_experience: List[WorkExperienceSchema]
    education: List[EducationSchema]
