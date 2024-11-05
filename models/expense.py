from backend import db  # Ensure correct import

class Expense(db.Model):
    __tablename__ = 'expenses'
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'))
    amount = db.Column(db.Float, nullable=False)
    contributor = db.Column(db.String(100))
    comment = db.Column(db.String(255))
    currency = db.Column(db.String(3))
    status = db.Column(db.String(50))  # Paid or Pending
