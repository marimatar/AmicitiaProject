from .initialization import db
from sqlalchemy.orm import declared_attr


class Details(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    gender = db.Column(db.String(20))
    age = db.Column(db.Integer)
    ethnicity = db.Column(db.String(50))
    interests = db.Column(db.JSON)  # Storing interests as JSON
    languages = db.Column(db.Text)
    bio = db.Column(db.Text)
    profile_picture_url = db.Column(db.String(255))

    @declared_attr
    def interests(cls):
        return db.Column(db.JSON, default=list)  # Default to an empty list
