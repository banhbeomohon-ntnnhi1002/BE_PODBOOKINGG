from infrastructure.databases import db
from datetime import datetime

class Rating(db.Model):
    __tablename__ = 'ratings'
    
    id = db.Column(db.Integer, primary_key=True)
    booking_id = db.Column(db.Integer, nullable=False)
    customer_id = db.Column(db.Integer, nullable=False)
    pod_id = db.Column(db.Integer, nullable=False)
    stars = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'booking_id': self.booking_id,
            'customer_id': self.customer_id,
            'pod_id': self.pod_id,
            'stars': self.stars,
            'comment': self.comment,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }