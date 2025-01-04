from flask import Blueprint, render_template, request
from flask_login import current_user, login_required


auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    pass

@auth.route('/register', methods=['GET', 'POST'])
def register():
    pass


@auth.route('/logout')
@login_required
def logout():
    pass