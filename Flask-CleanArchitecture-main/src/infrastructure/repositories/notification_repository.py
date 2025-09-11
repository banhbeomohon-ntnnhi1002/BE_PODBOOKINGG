from typing import List, Optional
from domain.models.notification import Notification
from domain.models.inotification_repository import INotificationRepository

class NotificationRepository(INotificationRepository):
    def __init__(self):
        self._notifications = []
        self._next_id = 1
    
    def add(self, notification: Notification) -> Notification:
        notification.id = self._next_id
        self._next_id += 1
        self._notifications.append(notification)
        return notification
    
    def get_by_customer_id(self, customer_id: int) -> List[Notification]:
        return [n for n in self._notifications if n.customer_id == customer_id]
    
    def mark_as_read(self, notification_id: int) -> bool:
        notification = next((n for n in self._notifications if n.id == notification_id), None)
        if notification:
            notification.is_read = True
            return True
        return False
    
    def get_unread_count(self, customer_id: int) -> int:
        return len([n for n in self._notifications if n.customer_id == customer_id and not n.is_read])