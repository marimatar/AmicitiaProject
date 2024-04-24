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


@app.route('/')
def index():
    return redirect(url_for('profile'))

@app.route('/home')
def home():  # put application's code here
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/homecommunity')
def homecommunity():
    return render_template('home-community.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

if __name__ == '__main__':
    app.run(debug=True)