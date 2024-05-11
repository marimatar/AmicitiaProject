from flask import Blueprint, render_template, request, flash, redirect, url_for, session, \
    jsonify  # views can be defined in multiple files
from . import db
from flask_login import login_user, login_required, logout_user, current_user
from .models import User, ProfileInfo
from .Details import Details

views = Blueprint('views', __name__)  # blueprint setup


@views.route('/')
def index():
    return redirect(url_for('auth.login'))


@views.route('/home', methods=['GET'])
def home():  # put application's code here
    return render_template('home.html')


# @views.route('/login')
# def loginpage():
#     return render_template('loginpage.html')


@views.route('/homecommunity')
def homecommunity():
    return render_template('home-community.html')


@views.route('/load')
def load():
    return render_template('load.html')


@views.route('/profile')
def profile():
    return render_template('profile.html', username = current_user.username)

@views.route('/match1')
def match1():
    return render_template('match1.html', username = current_user.username)

@views.route('/match2')
def match2():
    return render_template('match2.html', username = current_user.username)


@views.route('/match3')
def match3():
    return render_template('match3.html', username = current_user.username)

@views.route('/profileuser')
def profileuser():
    return render_template('profileuser.html', username=current_user.username, age=current_user.age,
                           gender=current_user.gender, ethnicity=current_user.ethnicity,
                           languages=current_user.languages, bio=current_user.bio)


@views.route('/chat')
def chat():
    return render_template('chat.html', username=current_user.username)

@views.route('/events')
def events():
    return render_template('events.html', username = current_user.username)

@views.route('/match')
def match():
    return render_template('match.html')
