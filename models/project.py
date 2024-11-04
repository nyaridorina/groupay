from app import db

class Project(db.Model):
    __tablename__ = 'projects'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    goal_amount = db.Column(db.Float, nullable=False)
    currency = db.Column(db.String(3), nullable=False)
    background_image_url = db.Column(db.String(255))
    is_archived = db.Column(db.Boolean, default=False)
