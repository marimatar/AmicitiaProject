from app import db

class Details(db.Model):
    __tablename__ = 'details'

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.Text,nullable=False)
    category = db.Column(db.String(50))

    def __repr__(self):
        return f"<Details(id='{self.id}', name='{self.name}', category='{self}, category='{self.category}')>"
