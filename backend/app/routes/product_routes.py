from flask import Blueprint, request, jsonify
from ..services.product_service import create_product_service, get_all_products_service, get_product_service, update_product_service, delete_product_service

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
        
@product_bp.route("/products", methods=['GET'])
def get_all_products():
    try:
        products = get_all_products_service()
        return jsonify(products), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400  

@product_bp.route("/products/<int:id>", methods=['GET'])
def get_product(id):
    try:
        product = get_product_service(id)
        return jsonify(product), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404

@product_bp.route("/products/<int:id>", methods=['PUT'])
def update_product(id):
    data = request.get_json()
    try:
        product = update_product_service(id, data)
        return jsonify(product), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    
@product_bp.route("/products/<int:id>", methods=['DELETE'])
def delete_product(id): 
    try:
        delete_product_service(id)
        return jsonify({"message": "Produto deletado com sucesso"}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404