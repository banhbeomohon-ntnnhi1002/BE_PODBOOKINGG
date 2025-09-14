from src.infrastructure.models.service_model import ServiceModel, AddonModel
from src.infrastructure.databases.session import db_session

class ServiceRepository:
    def get_all(self):
        return db_session.query(ServiceModel).all()

    def create(self, service: ServiceModel):
        db_session.add(service)
        db_session.commit()
        return service

class AddonRepository:
    def get_all(self):
        return db_session.query(AddonModel).all()

    def create(self, addon: AddonModel):
        db_session.add(addon)
        db_session.commit()
        return addon
