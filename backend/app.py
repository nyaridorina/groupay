import os
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

# Main entry point
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Use Render's PORT variable or default to 5000
    app.run(host="0.0.0.0", port=port)
