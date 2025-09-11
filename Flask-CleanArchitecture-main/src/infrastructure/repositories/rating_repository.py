from infrastructure.models.rating import Rating
from infrastructure.databases import db

class RatingRepository:
    def create(self, rating_data):
        rating = Rating(**rating_data)
        db.session.add(rating)
        db.session.commit()
        return rating
    
    def get_by_pod_id(self, pod_id):
        return Rating.query.filter_by(pod_id=pod_id).all()
    
    def get_all(self):
        return Rating.query.all()
    
    def get_by_id(self, rating_id):
        return Rating.query.get(rating_id)