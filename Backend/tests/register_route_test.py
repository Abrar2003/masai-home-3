import json
import pytest
from app import create_app
from app.extensions import db
from app.models.user import User

app = create_app()

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        with app.app_context():
            db.drop_all()

def test_register_valid_user(client):
    user_data = {
        "full_name": "Alice Smith",
        "email": "alice@example.com",
        "phone": "9876543210"
    }
    response = client.post('/auth/register', data=json.dumps(user_data), content_type='application/json')
    data = json.loads(response.data)
    assert response.status_code == 201  # 201 Created
    assert 'message' in data
    assert 'otp' in data

def test_register_missing_fields(client):
    user_data = {}  # Missing all fields
    response = client.post('/auth/register', data=json.dumps(user_data), content_type='application/json')
    data = json.loads(response.data)
    assert response.status_code == 400  # 400 Bad Request
    assert 'message' in data
    assert 'full name, email and phone are required' in data['message']

def test_register_invalid_email_format(client):
    user_data = {
        'full_name': 'Alice Smith',
        'email': 'invalid_email',  # Invalid email format
    }
    response = client.post('/auth/register', data=json.dumps(user_data), content_type='application/json')
    data = json.loads(response.data)
    assert response.status_code == 400  # 400 Bad Request
    assert 'message' in data
    assert 'Invalid email format' in data['message']

def test_register_invalid_phone_format(client):
    user_data = {
        'full_name': 'Alice Smith',
        'phone': '123',  # Invalid phone format
    }
    response = client.post('/auth/register', data=json.dumps(user_data), content_type='application/json')
    data = json.loads(response.data)
    assert response.status_code == 400  # 400 Bad Request
    assert 'message' in data
    assert 'Invalid phone number format' in data['message']

def test_register_existing_user(client):
    existing_user = User(full_name='Alice Smith', email='alice@example.com', phone='9876543210')
    with app.app_context():
        db.session.add(existing_user)
        db.session.commit()

    user_data = {
        'full_name': 'Bob Johnson',
        'email': 'alice@example.com',  # Email already exists
        'phone': '1234567890'
    }
    response = client.post('/auth/register', data=json.dumps(user_data), content_type='application/json')
    data = json.loads(response.data)
    assert response.status_code == 400  # 400 Bad Request
    assert 'message' in data
    assert 'Email or phone number already exists' in data['message']