# models/project.py
from backend import db  # Import db from backend instead of app

# Define your model here
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    goal_amount = db.Column(db.Float, nullable=False)
    currency = db.Column(db.String(3), nullable=False)
    background_image_url = db.Column(db.String(255))
    is_archived = db.Column(db.Boolean, default=False)

