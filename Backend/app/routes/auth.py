from flask import Blueprint, request, jsonify, session
from app.models.user import User
from app.extensions import db
import re
import string
import random


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

