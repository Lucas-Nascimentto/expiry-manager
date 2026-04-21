from flask import Blueprint, request, jsonify
from ..services.user_service import create_user_service, update_user_service, delete_user_service   

user_bp = Blueprint("user", __name__)   

@user_bp.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()

    try:
        user = create_user_service(data)

        return jsonify({
            "id": user.id,
            "name": user.name,
            "email": user.email
        }), 201

    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    
@user_bp.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.get_json()

    try:
        user = update_user_service(user_id, data)

        return jsonify({
            "id": user.id,
            "name": user.name,
            "email": user.email
        }), 200

    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@user_bp.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    try:
        delete_user_service(user_id)
        return jsonify({"message": "Usuário deletado com sucesso"}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404