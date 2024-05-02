from app import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    password = db.Column(db.String, unique=True, nullable=False)
    type = db.Column(db.String(50))

    __mapper_args__ = {
        'polymorphic_identity': 'user',
        'polymorphic_on': type
    }

    def __repr__(self):
        return f"<User(id={self.id}, username={self.username})>"


class Matcher(User):
    __tablename__ = 'matcher'
    id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)

    profileinfo = db.relationship('Profile', backref='matcher', lazy='True')

    __mapper_args__ = {
        'polymorphic_identity': 'matcher',
    }

    def __repr__(self):
        return f"<Matcher(id={self.id}, username={self.username})>"

class EventManager(User):
    __tablename__ = 'eventmanager'
    id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)

    __mapper_args__ = {'polymorphic_identity': 'eventmanager', }

    def __repr__(self):
        return f"<EventManager(id={self.id}, name={self.username})>"


class ProfileInfo(db.Model):
    __tablename__ = 'profileinfo'
    id = db.Column(db.Integer, primary_key=True)
    matcher_id = db.Column(db.Integer, db.ForeignKey('matcher'), nullable=False)
    details_id = db.Column(db.Integer, db.ForeignKey('details.id'), nullable=False)
    count = db.Column(db.Integer, nullable=False, default=0)

    details = db.relationship('Details')

    def __repr__(self):
        return f"<ProfileInfo(id={self.id}, matcher_id={self.matcher_id}, details_id={self.details_id}, count={self.count})>"
