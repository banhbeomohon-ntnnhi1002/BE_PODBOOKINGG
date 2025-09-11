from abc import ABC, abstractmethod
from typing import List, Optional
from .notification import Notification

class INotificationRepository(ABC):
    @abstractmethod
    def add(self, notification: Notification) -> Notification:
        pass
    
    @abstractmethod
    def get_by_customer_id(self, customer_id: int) -> List[Notification]:
        pass
    
    @abstractmethod
    def mark_as_read(self, notification_id: int) -> bool:
        pass
    
    @abstractmethod
    def get_unread_count(self, customer_id: int) -> int:
        pass