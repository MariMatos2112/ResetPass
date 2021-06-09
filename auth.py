from os import name
from flask import Blueprint, render_template, request, redirect, url_for
from flask.helpers import flash
from werkzeug.security import check_password_hash
from flask_login import login_user, logout_user, login_required
from .models import User

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password, password):
        flash('Seu usuário ou senha está incorreto.')
        return redirect(url_for('auth.login'))

    login_user(user)

    return redirect(url_for('main.index'))


@auth.route('/logout') 
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))


