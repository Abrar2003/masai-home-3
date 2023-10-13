from flask import Blueprint, request, jsonify, session
from app.models.user import User
from app.extensions import db

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/', methods=['GET'])
def hello():
    return "Hello, World!"

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    full_name = data.get('full_name')
    email = data.get('email')
    password = data.get('password')

    existing_user = User.query.filter_by(email=email).first()

    if existing_user:
        return jsonify({'message': 'Email already exists'}), 400

    new_user = User(full_name=full_name, email=email, password=password)
    
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully!'})

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    user = User.query.filter_by(email=email).first()

    if user and user.password == password:
        session['logged_in'] = True
        return jsonify({'message': 'Login successful!'})
    else:
        return jsonify({'message': 'Login failed'}, 401)

@auth_bp.route('/logout')
def logout():
    session.pop('logged_in', None)
    return jsonify({'message': 'Logged out'})
