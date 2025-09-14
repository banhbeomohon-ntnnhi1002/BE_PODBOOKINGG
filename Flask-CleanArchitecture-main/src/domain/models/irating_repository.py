from abc import ABC, abstractmethod
from typing import List, Optional
from .rating import Rating

class IRatingRepository(ABC):
    @abstractmethod
    def add(self, rating: Rating) -> Rating:
        pass
    
    @abstractmethod
    def get_by_id(self, rating_id: int) -> Optional[Rating]:
        pass
    
    @abstractmethod
    def get_by_booking_id(self, booking_id: int) -> Optional[Rating]:
        pass
    
    @abstractmethod
    def get_by_pod_id(self, pod_id: int) -> List[Rating]:
        pass
    
    @abstractmethod
    def update(self, rating: Rating) -> Rating:
        pass