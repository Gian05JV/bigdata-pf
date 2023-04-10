from flask import Flask
from config import Config
from models import db

def create_app():
    app_web = Flask(__name__)
    app_web.config.from_object(Config)
    app_web.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app_web)
    return app_web