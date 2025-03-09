from core.schemas import WorkExperienceSchema, WorkExperienceCreate
from typing import List
from abc import ABC, abstractmethod

class WorkExperienceServiceInterf(ABC):
    
    @abstractmethod
    def create_work(self, workExperience: WorkExperienceCreate) -> WorkExperienceSchema:
        pass

    @abstractmethod
    def update_work(self, work_id: int, workExperience: WorkExperienceSchema) -> WorkExperienceSchema:
        pass

    @abstractmethod
    def get_work_by_id(self, work_id: int) -> WorkExperienceSchema:
        pass

    @abstractmethod
    def get_works_by_user(self, user_id: int) -> List[WorkExperienceSchema]: 
        pass
