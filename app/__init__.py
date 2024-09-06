from flask import Flask
from app.auth import auth_bp
from app.evaluations import evaluations_bp
from app.report import report_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    # Register Blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(evaluations_bp)
    app.register_blueprint(report_bp)

    return app
