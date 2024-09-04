from flask import Blueprint, request, jsonify
from app.logic.admin_logic import  update_user, delete_user

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/admin/user', methods=['GET'])
def get_all_users():
    users = get_users()
    return jsonify(users)

@admin_bp.route('/admin/user', methods=['POST'])
def create_new_user():
    user_data = request.json
    user_id = create_user(user_data)
    return jsonify({'user_id': user_id}), 201

@admin_bp.route('/admin/user/<user_id>', methods=['PUT'])
def update_existing_user(user_id):
    user_data = request.json
    success = update_user(user_id, user_data)
    return jsonify({'success': success})

@admin_bp.route('/admin/user/<user_id>', methods=['DELETE'])
def delete_existing_user(user_id):
    success = delete_user(user_id)
    return jsonify({'success': success})
