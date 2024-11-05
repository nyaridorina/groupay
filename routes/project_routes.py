from flask import Blueprint, jsonify
from backend import db  # Ensure correct import
from models.project import Project

project_bp = Blueprint('projects', __name__)

@project_bp.route("/", methods=["GET"])
def get_projects():
    projects = Project.query.all()
    return jsonify([project.name for project in projects])
