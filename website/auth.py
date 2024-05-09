from flask import Blueprint, render_template, request, flash, redirect, url_for, session, jsonify  # views can be defined in multiple files
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from .models import User, ProfileInfo
import datetime


auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("loginpage.html", user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('views.home'))


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        birthday = request.form.get('birthday')

        user = User.query.filter_by(username=username).first()
        if password is None:
            flash('No password was provided.', category='error')
            return render_template("loginpage.html", user=current_user)
        if user:
            flash('Username is already taken.', category='error')
            return render_template("loginpage.html", user=current_user)
        if len(username) < 3:
            flash('username must be greater than 2 characters.', category='error')
            return render_template("loginpage.html", user=current_user)
        if len(password) < 7:
            flash('Password must be at least 7 characters.', category='error')
            return render_template("loginpage.html", user=current_user)

        try:
            birthday_date = datetime.datetime.strptime(birthday, '%Y-%m-%d')  # Use datetime.datetime
            today = datetime.datetime.now()
            age = today.year - birthday_date.year - ((today.month, today.day) < (birthday_date.month, birthday_date.day))
            if birthday_date > today:
                flash('Future birthdays are not valid.', category='error')
                return render_template("loginpage.html", user=current_user)
            if age < 18:
                flash('You must be at least 18 years old to register.', category='error')
                return render_template("loginpage.html", user=current_user)
        except ValueError:
            flash('Invalid date format.', category='error')
            return render_template("loginpage.html", user=current_user)

        new_user = User(
            username=username,
            password=generate_password_hash(password, method='pbkdf2:sha256'),
            birthday=birthday_date)
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user, remember=True)
        flash('Account created!', category='success')
        return redirect(url_for('views.profile'))

    return render_template("loginpage.html", user=current_user)
