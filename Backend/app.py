from flask import Flask, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'your_secret_key'  

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:chotu@localhost/flaskdb'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

@app.route('/register', methods=['POST'])
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

@app.route('/login', methods=['POST'])
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

@app.route('/logout')
def logout():
    
    session.pop('logged_in', None)
    return jsonify({'message': 'Logged out'})

@app.route('/users', methods=['GET'])
def see_users():
  
    if 'logged_in' in session:
        user_list = [{'full_name': user.full_name, 'email': user.email} for user in User.query.all()]
        return jsonify({'users': user_list})
    else:
        return jsonify({'message': 'Unauthorized. Please log in first.'}, 401)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
