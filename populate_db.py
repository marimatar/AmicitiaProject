from app import app, db
from User import User, Matcher, EventManager, ProfileInfo
from Details import Details

def clear_tables():

    Matcher.query.delete()
    ProfileInfo.query.delete()
    EventManager.query.delete()
    Details.query.delete()
    User.query.delete()
def populate_data():
    matcher1 = Matcher(username="Dorian", password="12345")
    manager1 = EventManager(name="AdminUser", password="adminpass")
    db.session.add(matcher1)
    db.session.add(manager1)

    db.session.commit()

    db.session.commit()

    def print_tables():
        """
        Print all data from the tables to the console.
        """
        print("Users:")
        for user in User.query.all():
            print(user)
        print("\nMatcher:")
        for matcher in Matcher.query.all():
            print(matcher)
        print("\nEventManagers:")
        for eventmanager in EventManager.query.all():
            print(eventmanager)

    if __name__ == '__main__':
        with app.app_context():
            db.create_all()
            # clear_tables()
            populate_data()
            print_tables()

