import datetime
from .initialization import db
from sqlalchemy.sql import func
from flask_login import UserMixin
from .Details import Details


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False)
    password = db.Column(db.String(150), nullable=False)
    birthday = db.Column(db.Date, nullable=False)
    gender = db.Column(db.String(20))
    pronouns = db.Column(db.String(20))
    ethnicity = db.Column(db.String(50))
    languages = db.Column(db.String(255))  # Comma-separated languages
    bio = db.Column(db.Text)

    @property
    def age(self):
        today = datetime.date.today()
        return today.year - self.birthday.year - ((today.month, today.day) < (self.birthday.month, self.birthday.day))



# class Matcher(User):
#     __tablename__ = 'matcher'
#     id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
#
#     profileinfo = db.relationship('Profile', backref='matcher', lazy='True')
#
#     __mapper_args__ = {
#         'polymorphic_identity': 'matcher',
#     }
#
#     def __repr__(self):
#         return f"<Matcher(id={self.id}, username={self.username})>"
#
# class EventManager(User):
#     __tablename__ = 'eventmanager'
#     id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
#
#     __mapper_args__ = {'polymorphic_identity': 'eventmanager', }
#
#     def __repr__(self):
#         return f"<EventManager(id={self.id}, name={self.username})>"


class ProfileInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    details_id = db.Column(db.Integer, db.ForeignKey('details.id'), nullable=False)
    count = db.Column(db.Integer, nullable=False, default=0)
    details = db.relationship('Details')


def populate_data():
    birthday_dorian = datetime.date(1990, 5, 15)  # Year, Month, Day
    birthday_mari = datetime.date(1992, 7, 22)
    user1 = User(username="Dorian", password="12345", birthday=birthday_dorian)
    user2 = User(username="mari", password="blahblah", birthday=birthday_mari)
    db.session.add(user1)
    db.session.add(user2)
    db.session.commit()
