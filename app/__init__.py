import os
from flask import Flask
from app.models import db

def create_app():
    app = Flask(__name__)

    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(BASE_DIR, 'tasks.db')}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    from app.routes import bp
    app.register_blueprint(bp)

    with app.app_context():
        db.create_all()

    return app