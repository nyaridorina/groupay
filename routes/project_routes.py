from flask import Blueprint, request, jsonify
from models.project import Project
from app import db

project_bp = Blueprint("project_bp", __name__)

@project_bp.route("/", methods=["GET"])
def get_projects():
    projects = Project.query.all()
    return jsonify([project.to_dict() for project in projects])

@project_bp.route("/", methods=["POST"])
def create_project():
    data = request.get_json()
    new_project = Project(
        name=data["name"],
        goal_amount=data["goal_amount"],
        currency=data["currency"],
        background_image_url=data.get("background_image_url")
    )
    db.session.add(new_project)
    db.session.commit()
    return jsonify(new_project.to_dict()), 201
