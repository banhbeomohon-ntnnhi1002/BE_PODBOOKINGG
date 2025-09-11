from flask import Blueprint, request, jsonify
from infrastructure.services.rating_service import RatingService
from api.schemas.rating import RatingRequestSchema, RatingResponseSchema

bp = Blueprint('rating', __name__, url_prefix='/ratings')

rating_service = RatingService()
request_schema = RatingRequestSchema()
response_schema = RatingResponseSchema()

@bp.route('/', methods=['GET'])
def get_all_ratings():
    """Get all ratings"""
    try:
        ratings = rating_service.get_all_ratings()
        return jsonify({
            'message': 'Success',
            'data': response_schema.dump(ratings, many=True)
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@bp.route('/', methods=['POST'])
def create_rating():
    """Create a new rating"""
    try:
        data = request.get_json()
        errors = request_schema.validate(data)
        if errors:
            return jsonify({'errors': errors}), 400
        
        rating = rating_service.create_rating(
            booking_id=data['booking_id'],
            customer_id=data['customer_id'],
            pod_id=data['pod_id'],
            stars=data['stars'],
            comment=data.get('comment')
        )
        return jsonify({
            'message': 'Rating created successfully',
            'data': response_schema.dump(rating)
        }), 201
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@bp.route('/pod/<int:pod_id>', methods=['GET'])
def get_pod_ratings(pod_id):
    """Get all ratings for a pod"""
    try:
        ratings = rating_service.get_pod_ratings(pod_id)
        average = rating_service.get_average_rating(pod_id)
        return jsonify({
            'message': 'Success',
            'data': {
                'ratings': response_schema.dump(ratings, many=True),
                'average_rating': round(average, 1),
                'total_ratings': len(ratings)
            }
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500