# routes/__init__.py

# Import blueprints so they can be easily accessed and registered in the main application
from .project_routes import project_bp
from .expense_routes import expense_bp

# Optionally, create a list of all blueprints for easier registration
blueprints = [
    (project_bp, "/api/projects"),
    (expense_bp, "/api/expenses")
]

