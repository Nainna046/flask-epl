from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    # ==================
    # CONFIG
    # ==================
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///epl.sqlite"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SECRET_KEY"] = "dev"  # ⭐⭐⭐ ตัวนี้ห้ามลืม

    # ==================
    # INIT EXTENSIONS
    # ==================
    db.init_app(app)

    # ==================
    # REGISTER BLUEPRINT
    # ==================
    from .routes import main
    app.register_blueprint(main)

    return app
