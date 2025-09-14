from sqlalchemy import Column, Integer, String, Float
from src.infrastructure.databases.base import Base

class ServiceModel(Base):
    __tablename__ = "services"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    description = Column(String(255))
    price = Column(Float, nullable=False)
    duration = Column(String(50), nullable=False)

class AddonModel(Base):
    __tablename__ = "addons"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    description = Column(String(255))
    price = Column(Float, nullable=False)
