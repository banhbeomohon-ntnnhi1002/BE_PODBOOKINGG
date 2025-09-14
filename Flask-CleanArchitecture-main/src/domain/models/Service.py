from dataclasses import dataclass

@dataclass
class Service:
    id: int
    name: str
    description: str
    price: float
    duration: str  # giờ, ngày, tuần, tháng

@dataclass
class Addon:
    id: int
    name: str
    description: str
    price: float
