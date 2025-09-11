from typing import List
from datetime import datetime
from domain.models.notification import Notification
from domain.models.inotification_repository import INotificationRepository

class NotificationService:
    def __init__(self, repository: INotificationRepository):
        self.repository = repository
    
    def create_booking_confirmation(self, customer_id: int, booking_id: int, 
                                  pod_name: str, booking_time: str) -> Notification:
        notification = Notification(
            id=None,
            customer_id=customer_id,
            booking_id=booking_id,
            title="Đặt chỗ thành công",
            message=f"Bạn đã đặt thành công pod {pod_name} vào {booking_time}",
            type="booking_confirmation",
            is_read=False,
            created_at=datetime.utcnow(),
            sent_at=datetime.utcnow()
        )
        return self.repository.add(notification)
    
    def create_reminder(self, customer_id: int, booking_id: int, 
                       pod_name: str, booking_time: str) -> Notification:
        notification = Notification(
            id=None,
            customer_id=customer_id,
            booking_id=booking_id,
            title="Nhắc nhở lịch đặt chỗ",
            message=f"Bạn có lịch đặt pod {pod_name} vào {booking_time}",
            type="reminder",
            is_read=False,
            created_at=datetime.utcnow(),
            sent_at=datetime.utcnow()
        )
        return self.repository.add(notification)
    
    def get_customer_notifications(self, customer_id: int) -> List[Notification]:
        return self.repository.get_by_customer_id(customer_id)
    
    def mark_as_read(self, notification_id: int) -> bool:
        return self.repository.mark_as_read(notification_id)