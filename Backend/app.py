from flask import Flask, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Set a secret key for session management.

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:1122@localhost/flaskdb'
db = SQLAlchemy(app)

# Define the User model with full_name, email, and phone_number
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=True)
    phone_number = db.Column(db.String(20), unique=True, nullable=True)
    verification_code = db.Column(db.String(6), nullable=True)

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    full_name = data.get('full_name')
    email = data.get('email')
    phone_number = data.get('phone_number')

    existing_user = User.query.filter((User.email == email) | (User.phone_number == phone_number)).first()

    if existing_user:
        return jsonify({'message': 'Email or phone number already exists'}), 400

    # Generate a 6-digit verification code
    verification_code = str(random.randint(100000, 999999))
    
    new_user = User(full_name=full_name, email=email, phone_number=phone_number, verification_code=verification_code)
    db.session.add(new_user)
    db.session.commit()

    # Send the verification code via email or SMS to the user

    return jsonify({'message': 'User registered. Please verify your email/phone number.'}), 201

@app.route('/verify', methods=['POST'])
def verify():
    data = request.get_json()
    email = data.get('email')
    phone_number = data.get('phone_number')
    verification_code = data.get('verification_code')

    user = User.query.filter((User.email == email) | (User.phone_number == phone_number)).first()

    if user and user.verification_code == verification_code:
        user.verification_code = None
        db.session.commit()
        return jsonify({'message': 'Verification successful!'})

    return jsonify({'message': 'Verification failed'}, 401)

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    phone_number = data.get('phone_number')

    user = User.query.filter((User.email == email) | (User.phone_number == phone_number)).first()

    if user and user.verification_code is None:
        # Set a session variable to indicate the user is logged in.
        session['logged_in'] = True
        return jsonify({'message': 'Login successful!'})
    else:
        return jsonify({'message': 'Login failed'}, 401)

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