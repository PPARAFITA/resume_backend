from core.schemas import SkillBase
from typing import List
from abc import ABC, abstractmethod

class SkillServiceInterf(ABC):
    @abstractmethod
    def create_skill(self, skill: SkillBase) -> SkillBase:
        pass

    @abstractmethod
    def get_skill_by_id(self, skillid: int) -> SkillBase:
        pass

    @abstractmethod
    def get_skills_by_userid(self, userid: int) -> List[SkillBase]: 
        pass

    @abstractmethod
    def update_skill(self, skillid: int, skill: SkillBase) -> SkillBase: 
        pass