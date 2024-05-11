from .initialization import db
from sqlalchemy.orm import declared_attr


class Details(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), unique=True)
    gender = db.Column(db.String(20))
    pronouns = db.Column(db.String(20))
    ethnicity = db.Column(db.String(50))
    languages = db.Column(db.String(255))  # Comma-separated languages
    bio = db.Column(db.Text)
