from .initialization import db

class Details(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.Text,nullable=False)
    category = db.Column(db.String(50))
