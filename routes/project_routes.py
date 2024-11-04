# routes/project_routes.py
from flask import Blueprint
from backend import db  # Corrected the import path to avoid circular dependency
from backend.models.project import Project

project_bp = Blueprint('projects', __name__)

@project_bp.route("/", methods=["GET"])
def get_projects():
    # Your logic to get projects
    return "List of projects"
