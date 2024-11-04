# backend/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from backend.config import Config  # Correct import for Config

# Initialize extensions globally
db = SQLAlchemy()
cors = CORS()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions with the app
    db.init_app(app)
    cors.init_app(app)

    # Import and register blueprints
    from backend.routes.project_routes import project_bp
    from backend.routes.expense_routes import expense_bp

    app.register_blueprint(project_bp, url_prefix="/api/projects")
    app.register_blueprint(expense_bp, url_prefix="/api/expenses")

    return app
