from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import db, User

account_bp = Blueprint('account_bp', __name__)

@account_bp.route("/info", methods=["GET"])
@jwt_required()
def get_account_info():
    """Lấy thông tin tài khoản của người dùng đã xác thực."""
    current_user_email = get_jwt_identity()
    user = User.query.filter_by(user_email=current_user_email).first()
    
    if user:
        return jsonify({
            "id": user.id,
            "email": user.user_email
        }), 200
    
    return jsonify({"message": "Không tìm thấy người dùng"}), 404