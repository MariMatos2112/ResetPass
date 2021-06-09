from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from werkzeug.security import generate_password_hash
from . import db
from .models import User

main = Blueprint('main', __name__)

@main.route('/')
@login_required
def index():
    return render_template('index.html', name=current_user.name)

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)

@main.route('/profile', methods=['POST'])
def profile_post():
    name = request.form.get('name')
    email = request.form.get('email')
    new_password = request.form.get('new_password')

    print(name, email, new_password)

    new_user = User(name=name, email=email, password=generate_password_hash(new_password, method='sha256'))
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('main.index'))
