from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required, login_user, logout_user

from rondo.auth.utils import get_permission_objects
from rondo.models.roles_permissions import Role
from rondo.models.users import Users
from rondo.extensions import db, bcrypt
from rondo.defaults import DEFAULT_ROLE_PERMISSIONS


auth = Blueprint('auth', __name__)

@auth.route("/")
@auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('superadmin.dashboard'))
    
    if request.method == "POST":
        username = request.form["username"].strip().lower()
        password = request.form["password"].strip()

        admin = db.session.execute(db.select(Users).filter_by(username=username)).first()
        if not admin:
            flash("Password or username incorrect", "danger")
            return render_template("auth/login.html")
        
        if not bcrypt.check_password_hash(admin[0].password, password):
            flash("Password or username incorrect", "danger")
            return render_template("auth/login.html")
        
        login_user(admin[0])
        next_page = request.args.get("next")
        return redirect(next_page) if next_page else redirect(url_for("superadmin.dashboard"))
    
    return render_template("auth/login.html")

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        name = request.form["full-name"].strip()
        username = request.form["username"].strip().lower()
        email = request.form["email"].strip()
        password = request.form["password"].strip()
        confirm_password = request.form["confirm-password"].strip()

        user = db.session.execute(db.select(Users).filter_by(username=username)).first()
        emails = db.session.execute(db.select(Users).filter_by(email=email)).first()

        if password != confirm_password:
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

        # add the new permissions
        for perm in get_permission_objects(DEFAULT_ROLE_PERMISSIONS[role[0].name]):
            new_user.permissions.append(perm[0])

        db.session.add(new_user)
        db.session.commit()
        
        flash("Account successfully created. Now login", "success")
        return redirect(url_for("auth.login"))

    return render_template("auth/register.html")


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Logout Successful!", "info")
    return redirect(url_for("auth.login"))
