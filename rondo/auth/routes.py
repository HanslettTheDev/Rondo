from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required

from rondo.models.roles_permissions import Role
from rondo.models.users import Users
from rondo.extensions import db, bcrypt


auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    
    return render_template('auth/login.html')

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        name = request.form["full-name"].strip()
        username = request.form["full-name"].strip()
        email = request.form["username"].strip()
        password = request.form["password"].strip()
        confirm_password = request.form["confirm-password"].strip()

        user = db.session.execute(db.select(Users).filter_by(username=username)).first()
        emails = db.session.execute(db.select(Users).filter_by(email=email)).first()

        if password != confirm_password:
            print(password, confirm_password)
            flash("Passwords do not match", "danger")
            return redirect(url_for('auth.register'))
        
        if user or emails:
            flash("Username or Email already taken", "danger")

        new_user = Users(
            username=username, name=name, 
            email=email, password=bcrypt.generate_password_hash(password)
        )
        role = db.session.execute(db.select(Role).filter_by(name="user")).first()
        new_user.role = role[0]

        db.session.add(new_user)
        db.session.commit()
        
        flash("Account successfully created. Now login", "success")
        return redirect(url_for("auth.login"))


        

    return render_template('auth/register.html')


@auth.route('/logout')
@login_required
def logout():
    pass