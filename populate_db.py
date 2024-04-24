from app import app, db
from User import User

def clear_tables():

    User.query.delete()

# def populate_data():
