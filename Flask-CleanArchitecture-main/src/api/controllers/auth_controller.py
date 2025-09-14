from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from models import db, User
import uuid

auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route("/signup", methods=["POST"])
def signup():
    """Endpoint đăng ký tài khoản mới."""
    data = request.json
    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({"message": "Vui lòng cung cấp cả email và mật khẩu."}), 400

    # Kiểm tra xem email đã tồn tại chưa
    existing_user = User.query.filter_by(user_email=email).first()
    if existing_user:
        return jsonify({"message": "Email đã tồn tại. Vui lòng đăng nhập."}), 409

    # Tạo người dùng mới và lưu vào cơ sở dữ liệu
    new_user = User(
        id=str(uuid.uuid4()),
        user_email=email,
        password=password  # Lưu ý: Trong môi trường thực tế cần hash mật khẩu
    )
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "Đăng ký thành công!"}), 201

@auth_bp.route("/login", methods=["POST"])
def login():
    """Endpoint đăng nhập."""
    data = request.json
    email = data.get("email")
    password = data.get("password")
    
    # Tìm kiếm người dùng trong cơ sở dữ liệu
    user = User.query.filter_by(user_email=email, password=password).first()
    
    if user:
        # Nếu tìm thấy, tạo JWT token và trả về
        access_token = create_access_token(identity=email)
        return jsonify(access_token=access_token), 200
    
    return jsonify({"message": "Tài khoản hoặc mật khẩu không đúng!"}), 401