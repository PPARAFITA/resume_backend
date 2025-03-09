from core.schemas import UserBase, User
from typing import List
from abc import ABC, abstractmethod

class UserServiceInterf(ABC):
    @abstractmethod
    def create_user(self, user: UserBase) -> User:
        pass

    @abstractmethod
    def get_user_by_id(self, user_id: int) -> User:
        pass

    @abstractmethod
    def get_users(self) -> List[User]: 
        pass

    @abstractmethod
    def update_user(self, user_id: int, user: UserBase) -> User: 
        pass