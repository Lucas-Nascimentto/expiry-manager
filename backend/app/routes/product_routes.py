from flask import Blueprint, request, jsonify
from app.services.product_service import create_product_service

product_bp = Blueprint("product", __name__)

@product_bp.route("/products", methods=["POST"])
def create_product():
    data = request.get_json()

    try:
        product = create_product_service(data)

        return jsonify({
            "id": product.id,
            "name": product.name
        }), 201

    except ValueError as e:
        return jsonify({"error": str(e)}), 400