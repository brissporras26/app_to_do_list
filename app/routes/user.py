from flask import Blueprint, request, jsonify
from app.logic.users_logic import get_profile, create_profile, delete_profile, update_profile

user_bp = Blueprint('user', __name__)

@user_bp.route('/profile', methods=['GET'])
def get_user_profile():
    email = request.args.get('email')
    if not email:
        return jsonify({'error': 'El email es requerido.'}), 400

    profile = get_profile(email)
    if not profile:
        return jsonify({'error': 'Perfil no encontrado.'}), 404

    return jsonify(profile), 200

@user_bp.route('/profile', methods=['POST'])
def create_user_profile():
    data = request.json
    name = data.get('name')
    email = data.get('email')

    if not name or not email:
        return jsonify({'error': 'Nombre y email son requeridos.'}), 400

    profile_id = create_profile(name, email)
    if not profile_id:
        return jsonify({'error': 'El usuario ya existe.'}), 400

    return jsonify({'message': 'Perfil creado correctamente.', 'profile_id': str(profile_id)}), 201

@user_bp.route('/profile', methods=['DELETE'])
def delete_user_profile():
    email = request.args.get('email')
    if not email:
        return jsonify({'error': 'El email es requerido.'}), 400

    success = delete_profile(email)
    if not success:
        return jsonify({'error': 'El usuario no existe.'}), 404

    return jsonify({'message': 'Perfil eliminado correctamente.'}), 200

@user_bp.route('/profile', methods=['PUT'])
def update_user_profile():
    data = request.json
    email = data.get('email')
    new_email = data.get('new_email')

    if not email or not new_email:
        return jsonify({'error': 'Email y nuevo email son requeridos.'}), 400

    success = update_profile(email, new_email)
    if not success:
        return jsonify({'error': 'El usuario no existe.'}), 404

    return jsonify({'message': 'Perfil actualizado correctamente.'}), 200
