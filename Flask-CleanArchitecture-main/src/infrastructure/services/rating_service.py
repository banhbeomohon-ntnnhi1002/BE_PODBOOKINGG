from infrastructure.repositories.rating_repository import RatingRepository

class RatingService:
    def __init__(self, rating_repository=None):
        self.rating_repository = rating_repository or RatingRepository()
    
    def create_rating(self, booking_id, customer_id, pod_id, stars, comment=None):
        if not (1 <= stars <= 5):
            raise ValueError("Stars must be between 1 and 5")
        
        rating_data = {
            'booking_id': booking_id,
            'customer_id': customer_id,
            'pod_id': pod_id,
            'stars': stars,
            'comment': comment
        }
        return self.rating_repository.create(rating_data)
    
    def get_pod_ratings(self, pod_id):
        return self.rating_repository.get_by_pod_id(pod_id)
    
    def get_average_rating(self, pod_id):
        ratings = self.get_pod_ratings(pod_id)
        if not ratings:
            return 0
        return sum(r.stars for r in ratings) / len(ratings)
    
    def get_all_ratings(self):
        return self.rating_repository.get_all()