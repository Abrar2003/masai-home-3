from flask import Blueprint, request, jsonify, session, make_response
from app.models.user import User
from app.extensions import db
import re
import string
import random
import jwt


auth_bp = Blueprint('auth', __name__)

def is_email(input):
    return re.match(r"[^@]+@[^@]+\.[^@]+", input) is not None

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    full_name = data.get('full_name')
    email = data.get('email')
    phone = data.get('phone')

    existing_user = User.query.filter((User.email == email) | (User.phone == phone)).first()

    if existing_user:
        return jsonify({'message': 'Email or phone number already exists'}), 400
    else:
        otp = ''.join(random.choices(string.digits, k=6))
        new_user = User(full_name=full_name, email=email, phone=phone, otp=otp)
        db.session.add(new_user)
        db.session.commit()

        return jsonify({'message': 'User registered successfully', 'otp': otp})


@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    key = data.get('key')

    # Validate if the input is an email or phone
    if is_email(key):
        user = User.query.filter_by(email=key).first()
    else:
        user = User.query.filter_by(phone=key).first()

    if user:
        # Generate a random 6-digit OTP
        otp = ''.join(random.choices(string.digits, k=6))
        user.otp = otp
        db.session.commit()
        return jsonify({'message': 'Please verify the OTP', 'otp': otp})
    else:
        return jsonify({'message': 'Please register. The email or phone number does not exist'}), 404

@auth_bp.route('/verify', methods=['POST'])
def verify():
    data = request.get_json()
    key = data.get('key')
    user_otp = data.get('otp')

    if is_email(key):
        existing_user = User.query.filter_by(email=key).first()
    else:
        existing_user = User.query.filter_by(phone=key).first()

    if existing_user:
        if user_otp == existing_user.otp:
            # Generate a token
            token = jwt.encode({'email': existing_user.email}, 'your-secret-key', algorithm='HS256')

            # Create a response with the token and set the session cookie
            response = make_response(jsonify({'message': 'OTP verification successful', 'name': existing_user.full_name, 'email': existing_user.email}))
            response.set_cookie('login_token', token, path='/')  # Set the session cookie

        else:
            return jsonify({'message': 'Invalid OTP'}), 400
    else:
        return jsonify({'message': 'User not found'}), 404


@auth_bp.route('/logout')
def logout():
    session.pop('logged_in', None)
    return jsonify({'message': 'Logged out'})
