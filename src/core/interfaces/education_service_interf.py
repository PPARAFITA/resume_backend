from abc import ABC, abstractmethod
from typing import List
from core.schemas import EducationSchema, EducationCreate

class EducationServiceInterf(ABC):

    @abstractmethod
    def create_education(self, education: EducationCreate) -> EducationSchema:
        pass

    @abstractmethod
    def get_education_by_id(self, education_id: int) -> EducationSchema:
        pass

    @abstractmethod
    def get_educations_by_user(self,user_id: int) -> List[EducationSchema]: 
        pass