from flask import Blueprint, request, jsonify

service_bp = Blueprint("service", __name__, url_prefix="/api")

# Fake database in-memory
services = []
addons = []

# --------- Services ----------
@service_bp.route("/services", methods=["GET"])
def get_services():
    return jsonify(services), 200

@service_bp.route("/services", methods=["POST"])
def create_service():
    data = request.json
    if not data.get("name") or not data.get("price") or not data.get("duration"):
        return jsonify({"error": "Missing required fields"}), 400

    service = {
        "id": len(services) + 1,
        "name": data["name"],
        "description": data.get("description", ""),
        "price": data["price"],
        "duration": data["duration"]
    }
    services.append(service)
    return jsonify(service), 201

# --------- Addons ----------
@service_bp.route("/addons", methods=["GET"])
def get_addons():
    return jsonify(addons), 200

@service_bp.route("/addons", methods=["POST"])
def create_addon():
    data = request.json
    if not data.get("name") or not data.get("price"):
        return jsonify({"error": "Missing required fields"}), 400

    addon = {
        "id": len(addons) + 1,
        "name": data["name"],
        "description": data.get("description", ""),
        "price": data["price"]
    }
    addons.append(addon)
    return jsonify(addon), 201
