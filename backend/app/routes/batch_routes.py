from flask import Blueprint, request, jsonify
from ..services.batch_service import create_batch_service, get_batch_service, get_all_batches_service, update_batch_service, delete_batch_service

batch_bp = Blueprint('batch', __name__) 

@batch_bp.route('/batches', methods=['POST'])
def create_batch():
    data = request.get_json()
    try:
        batch = create_batch_service(data)
        return jsonify(batch), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@batch_bp.route('/batches', methods=['GET'])
def get_all_batches():
    batches = get_all_batches_service()
    return jsonify(batches), 200

@batch_bp.route('/batches/<int:id>', methods=['GET'])
def get_batch(id):
    try:
        batch = get_batch_service(id)
        return jsonify(batch), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404

@batch_bp.route('/batches/<int:id>', methods=['PUT'])
def update_batch(id):
    data = request.get_json()
    try:
        batch = update_batch_service(id, data)
        return jsonify(batch), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@batch_bp.route('/batches/<int:id>', methods=['DELETE'])
def delete_batch(id):
    try:
        delete_batch_service(id)
        return jsonify({"message": "Batch deletado com sucesso"}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404
    