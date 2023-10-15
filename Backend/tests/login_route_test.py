import json
import pytest
from app import create_app
from app.extensions import db
from app.models.user import User
from unittest.mock import patch

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

def test_login_valid_email(client):
    with patch('random.choices', return_value=['1', '2', '3', '4', '5', '6']):
        user = User(full_name='Alice Smith', email='alice@example.com', phone='9876543210')
        with app.app_context():
            db.session.add(user)
            db.session.commit()

        response = client.post('/auth/login', json={'key': 'alice@example.com'})
        data = json.loads(response.data)
        assert response.status_code == 200
        assert 'otp' in data
        assert data['otp'] == '123456'  # Mocked random OTP

def test_login_valid_phone(client):
    with patch('random.choices', return_value=['1', '2', '3', '4', '5', '6']):
        user = User(full_name='Bob', email='bob@example.com', phone='1234567890')
        with app.app_context():
            db.session.add(user)
            db.session.commit()

        response = client.post('/auth/login', json={'key': '1234567890'})
        data = json.loads(response.data)
        assert response.status_code == 200
        assert 'otp' in data
        assert data['otp'] == '123456'  # Mocked random OTP

def test_login_invalid_key(client):
    response = client.post('/auth/login', json={'key': 'invalid_key'})
    data = json.loads(response.data)
    assert response.status_code == 400
    assert 'message' in data
    assert data['message'] == 'Please enter a valid email or phone number'

def test_login_user_not_found(client):
    response = client.post('/auth/login', json={'key': 'nonexistent@example.com'})
    data = json.loads(response.data)
    assert response.status_code == 404
    assert 'message' in data
    assert data['message'] == 'Please register. The email or phone number does not exist'
