from flask import Blueprint, jsonify, session
from app.models.user import User

user_bp = Blueprint('user', __name__)

@user_bp.route('/users', methods=['GET'])
def see_users():
    if 'logged_in' in session:
        user_list = [{'full_name': user.full_name, 'email': user.email} for user in User.query.all()]
        return jsonify({'users': user_list})
    else:
        return jsonify({'message': 'Unauthorized. Please log in first.'}, 401)
