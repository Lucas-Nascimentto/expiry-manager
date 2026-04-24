from flask import Blueprint, request, jsonify
from ..services.auth_service import login_service

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    try:
        result = login_service(data)
        return jsonify(result), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 401