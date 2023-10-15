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

def is_phone(phone):
    # Define a regular expression pattern for a ten-digit phone number.
    phone_pattern = r"^\d{10}$"

    # Use the re.match() function to check if the phone matches the pattern.
    if re.match(phone_pattern, phone):
        return True
    else:
        return False

@auth_bp.route("/", methods=['GET'])
def hello():
    return 'Hello, World!'

@auth_bp.route('/register', methods=['POST'])
def register():
    # try:
        data = request.get_json()
        full_name = data.get('full_name')
        email = data.get('email')
        phone = data.get('phone')

        # Validation: Check if required fields are provided.
        if not full_name or not (email or phone):
            return jsonify({'message': 'full name, email and phone are required'}), 400

        # Validation: Check email format (optional).
        if email and not is_email(email):
            return jsonify({'message': 'Invalid email format'}), 400

        # Validation: Check phone format (optional).
        if phone and not is_phone(phone):
            return jsonify({'message': 'Invalid phone number format'}), 400

        existing_user = User.query.filter((User.email == email) | (User.phone == phone)).first()

        if existing_user:
            return jsonify({'message': 'Email or phone number already exists'}), 400
        else:
            otp = ''.join(random.choices(string.digits, k=6))
            new_user = User(full_name=full_name, email=email, phone=phone, otp=otp)
            db.session.add(new_user)
            db.session.commit()

            return jsonify({'message': 'User registered successfully', 'otp': otp}),201
        
    # except Exception as e:
    #     return jsonify({'message': 'An error occurred while registering the user'}), 500


@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    key = data.get('key')

    # Check if the input is an email or phone number
    if is_email(key):
        user = User.query.filter_by(email=key).first()
    elif is_phone(key):
        user = User.query.filter_by(phone=key).first()
    else:
        return jsonify({'message': 'Please enter a valid email or phone number'}), 400

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
    elif is_phone(key):
        existing_user = User.query.filter_by(phone=key).first()
    else :
        return jsonify({'message': 'Please enter a valid email or phone number'}), 400

    if existing_user:
        if user_otp == existing_user.otp:
           # Generate a token
            token = jwt.encode({'email': existing_user.email}, 'your-secret-key', algorithm='HS256')
            response.set_cookie('user_name', existing_user.full_name, path='/')  # Set the session cookie
            # Create a response with the token and set the session cookie
            response = make_response(jsonify({'message': 'OTP verification successful', 'name': existing_user.full_name, 'email': existing_user.email}))
            response.set_cookie('login_token', token, path='/')  # Set the session cookie
            return response
        else:
            return jsonify({'message': 'Invalid OTP'}), 400
    else:
        return jsonify({'message': 'User not found, Please try again with a registered email or phone number'}), 404


@auth_bp.route('/logout')
def logout():
    session.pop('logged_in', None)
    return jsonify({'message': 'Logged out'})
