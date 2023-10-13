from flask import Flask
from app.config import Config
from app.extensions import db
from app.models.user import User
from app.routes.auth import auth_bp
from app.routes.user import user_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    

    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(user_bp, url_prefix='/user')

    return app
