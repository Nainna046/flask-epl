from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__, template_folder="templates")

    # ========================
    # CONFIG
    # ========================
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///epl.sqlite"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SECRET_KEY"] = "dev"  # ⭐ สำคัญมากสำหรับ flash

    # ========================
    # INIT EXTENSIONS
    # ========================
    db.init_app(app)

    # ========================
    # REGISTER BLUEPRINT
    # ========================
    from .routes import main
    app.register_blueprint(main)

    return app
