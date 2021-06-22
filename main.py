from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask import *
from flask_login import login_required, current_user
from werkzeug.security import generate_password_hash
from . import db
from .models import User
import subprocess

main = Blueprint('main', __name__)

@main.route('/')
@login_required
def index():
    return render_template('index.html', name=current_user.name)

@main.route('/', methods=['POST'])
def index_post():
    login = request.form.get('ad_user_login')

    try:
        change_password = f'Set-ADAccountPassword -Identity {login} -NewPassword (ConvertTo-SecureString -AsPlainText "Marvel@112233" -Force)'
        unlock_user = f'Unlock-ADAccount -Identity {login}'
        change_password_at_logon = f'Set-ADUser -Identity {login} -ChangePasswordAtLogon $true'
        subprocess.check_output(f"PowerShell -Executionpolicy byPass -Command {change_password}")
        subprocess.check_output(f"PowerShell -Executionpolicy byPass -Command {unlock_user}")
        subprocess.check_output(f"PowerShell -Executionpolicy byPass -Command {change_password_at_logon}")
        flash('Senha alterada com sucesso!')
    except:
        flash('Usuário não existe :(')

    return redirect(url_for('main.index'))


@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name, email=current_user.email)

@main.route('/profile', methods=['POST'])
def profile_post():
    name = current_user.name
    email = current_user.email
    new_password = request.form.get('new_password')
    new_password_confirmation = request.form.get('new_password_confirmation')

    if new_password == new_password_confirmation:
        user = User.query.filter_by(email=email).first()
        user.password = generate_password_hash(new_password, method='sha256')
        db.session.commit()
        flash('Sua senha foi alterada com sucesso!')
    else:
        flash('As senhas não coincidem :(')

    return redirect(url_for('main.profile'))