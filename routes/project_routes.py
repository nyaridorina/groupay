from flask import Blueprint, jsonify
from backend import db  # db is correctly imported from backend
from models.project import Project  # Corrected the import path for Project model

project_bp = Blueprint('projects', __name__)

@project_bp.route("/", methods=["GET"])
def get_projects():
    projects = Project.query.all()
    return jsonify([project.name for project in projects])
