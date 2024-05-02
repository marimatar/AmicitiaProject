import os
from flask import Flask, jsonify, flash, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.secret_key = 'amicitia101!'

app.config['SQLALCHEMY_DATABASE_URI'] = \
    'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from Details import Details
from User import User, Matcher, EventManager, ProfileInfo
from flask import Flask, render_template, request, redirect, session
from sqlalchemy.exc import IntegrityError


def index():
    return redirect(url_for('profile'))


class ApiCalls:
    @staticmethod
    @app.route('/api/addUser', methods=['POST'])
    def addUser():
        username = request.form.get('username')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        # Check if any field is empty
        if not all([username, password, confirm_password]):
            flash("All fields must be filled out", "error")  # Using flash for error message
            return redirect(url_for('regnlog'))  # Redirect back to the form

        # Check password confirmation
        if password != confirm_password:
            flash("Passwords do not match", "error")  # 'error' is the category
            return redirect(url_for('regnlog'))  # Redirect to the user login page

        # Attempt to add user to database
        try:
            new_user = Matcher(username=username, password=password)
            db.session.add(new_user)
            db.session.commit()
            flash("User added successfully", "success")  # 'success' is a category
            return redirect(url_for('regnlog'))  # Redirect to the form page
        except Exception as e:
            flash("An error occurred. Please try again.", "error")
            return redirect(url_for('regnlog'))

    @app.route('/api/login', methods=['POST'])
    def login(self):
        username = request.form.get('userName')
        password = request.form.get('passWord')

        user = db.session.query(User).filter(User.name == username, User.password == password).first()

        if not user:
            flash("Sign in unsuccessful. Please try again.", "error")
            return redirect(url_for('regnlog'))
        else:
            session['logged_in'] = True
            session['username'] = user.username
            session['user_id'] = user.id
            session['user_type'] = user.type
            return render_template('home-community.html', session=session)

    @staticmethod
    @app.route('/api/logout', methods=['POST'])
    def logout():
        if 'logged_in' in session:
            session.pop('logged_in', None)
            session.pop('username', None)
            session.pop('user_id', None)
        return render_template('home-community.html', session=session)


# These app routes are 'URL' requests. A function will be run whenever the web page reaches any of these URLs.
@app.route('/')
@app.route('/home')
def home():  # put application's code here
    return render_template('home.html')


@app.route('/regnlog')
def regnlog():
    return render_template('regnlog.html')


@app.route('/homecommunity')
def homecommunity():
    return render_template('home-community.html')


@app.route('/profile')
def profile():
    return render_template('profile.html')


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
