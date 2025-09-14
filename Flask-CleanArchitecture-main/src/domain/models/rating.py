from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class Rating:
    id: Optional[int]
    booking_id: int
    customer_id: int
    pod_id: int
    stars: int  # 1-5
    comment: Optional[str]
    created_at: datetime
    updated_at: datetime