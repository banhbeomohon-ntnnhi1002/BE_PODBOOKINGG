from src.infrastructure.models.service_model import ServiceModel, AddonModel
from src.infrastructure.repositories.service_repository import ServiceRepository, AddonRepository

class ServiceService:
    def __init__(self, repo: ServiceRepository):
        self.repo = repo

    def list_services(self):
        return self.repo.get_all()

    def create_service(self, name, description, price, duration):
        service = ServiceModel(name=name, description=description, price=price, duration=duration)
        return self.repo.create(service)

class AddonService:
    def __init__(self, repo: AddonRepository):
        self.repo = repo

    def list_addons(self):
        return self.repo.get_all()

    def create_addon(self, name, description, price):
        addon = AddonModel(name=name, description=description, price=price)
        return self.repo.create(addon)
