from flask import Flask, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
import re
import string
import random
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.secret_key = 'your_secret_key'  # Set a secret key for session management.

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:1234@localhost/flaskdb'
db = SQLAlchemy(app)

# Define the User model with full_name, email, and phone_number
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=True)
    phone = db.Column(db.String(20), unique=True, nullable=True)
    otp = db.Column(db.String(6), nullable=True)

def is_email(input):
    return re.match(r"[^@]+@[^@]+\.[^@]+", input) is not None

@app.route("/",methods=["GET"])
def hello ():
    return "HELL!!!"
@app.route('/register', methods=['POST'])
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


@app.route('/verify', methods=['POST'])
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
            return jsonify({'message': 'OTP verification successful', 'name': existing_user.full_name, 'email': existing_user.email})
        else:
            return jsonify({'message': 'Invalid OTP'}), 400
    else:
        return jsonify({'message': 'User not found'}), 404

@app.route('/login', methods=['POST'])
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

        
@app.route('/logout')
def logout():
    # Clear the session variable to log the user out.
    session.pop('logged_in', None)
    return jsonify({'message': 'Logged out'})

@app.route('/users', methods=['GET'])
def see_users():
    # Check if the user is logged in before showing user data.
    if 'logged_in' in session:
        user_list = [{'full_name': user.full_name, 'email': user.email, 'phone_number': user.phone_number} for user in User.query.all()]
        return jsonify({'users': user_list})
    else:
        return jsonify({'message': 'Unauthorized. Please log in first.'}, 401)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)