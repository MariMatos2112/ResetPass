from . import db
from .models import User

def add_user(user_name, user_email, user_password):
    new_user = User(name=user_name, email=user_email, password=user_password)
    db.session.add(new_user)
    db.session.commit()

