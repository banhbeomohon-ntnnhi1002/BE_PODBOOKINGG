from flask import Blueprint, request, jsonify
from infrastructure.services.notification_service import NotificationService
from infrastructure.repositories.notification_repository import NotificationRepository
from api.schemas.notification import NotificationResponseSchema

bp = Blueprint('notification', __name__, url_prefix='/notifications')

notification_service = NotificationService(NotificationRepository())
response_schema = NotificationResponseSchema()

@bp.route('/customer/<int:customer_id>', methods=['GET'])
def get_customer_notifications(customer_id):
    """Get all notifications for a customer"""
    notifications = notification_service.get_customer_notifications(customer_id)
    return jsonify(response_schema.dump(notifications, many=True)), 200

@bp.route('/<int:notification_id>/read', methods=['PUT'])
def mark_notification_read(notification_id):
    """Mark notification as read"""
    success = notification_service.mark_as_read(notification_id)
    if success:
        return jsonify({'message': 'Notification marked as read'}), 200
    return jsonify({'error': 'Notification not found'}), 404

@bp.route('/booking-confirmation', methods=['POST'])
def send_booking_confirmation():
    """Send booking confirmation notification"""
    data = request.get_json()
    notification = notification_service.create_booking_confirmation(
        customer_id=data['customer_id'],
        booking_id=data['booking_id'],
        pod_name=data['pod_name'],
        booking_time=data['booking_time']
    )
    return jsonify(response_schema.dump(notification)), 201