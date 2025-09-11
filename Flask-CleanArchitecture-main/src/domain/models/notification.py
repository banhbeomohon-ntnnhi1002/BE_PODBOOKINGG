from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class Notification:
    id: Optional[int]
    customer_id: int
    booking_id: int
    title: str
    message: str
    type: str  # 'booking_confirmation', 'reminder', 'rating_request'
    is_read: bool
    created_at: datetime
    sent_at: Optional[datetime]