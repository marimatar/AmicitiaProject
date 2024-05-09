from flask import Blueprint, render_template, redirect, url_for  # views can be defined in multiple files using Blueprint
from . import db
from flask_login import login_required, current_user
from .models import User, ProfileInfo

views = Blueprint('views', __name__)  # blueprint setup


def index():
    return redirect(url_for('views.profile'))


@views.route('/')
@views.route('/home', methods=['GET'])
def home():  # put application's code here
    return render_template('home.html')


@views.route('/login')
def loginpage():
    return render_template('loginpage.html')


@views.route('/homecommunity')
def homecommunity():
    return render_template('home-community.html')


@views.route('/profile')
def profile():
    return render_template('profile.html')

@views.route('/chat')
def chat():
    return render_template('chat.html')

@views.route('/match')
def match():
    return render_template('match.html')
