import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from routes.project_routes import project_bp
from routes.expense_routes import expense_bp
from backend import create_app  # Ensure correct import

# Create the Flask app instance using the factory function
app = create_app()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
