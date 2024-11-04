# app.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from routes.project_routes import project_bp
from routes.expense_routes import expense_bp

app = Flask(__name__)
app.config.from_object("config.Config")
db = SQLAlchemy(app)
CORS(app)

# Register Blueprints
app.register_blueprint(project_bp, url_prefix="/api/projects")
app.register_blueprint(expense_bp, url_prefix="/api/expenses")

# Ensure the app runs only if called directly (for local testing)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
