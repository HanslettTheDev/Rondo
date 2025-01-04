from flask import Blueprint, jsonify, render_template, url_for
from rondo.extensions import db, bcrypt
from rondo.models.users import Users
from rondo.models.roles_permissions import Role, UserRoles, Permissions
from rondo.models.logs import Logs
from rondo.models.laptop import LaptopTable, laptopIventory

admin = Blueprint("admin", __name__)

@admin.route("/")
@admin.route("/dashboard")
def dashboard():
    return render_template("admin/main.html", title="Dashboard")


@admin.route("/fill")
def fill():
    # role = Role()
    # role.add_default_roles()

    # permission = Permissions()
    # permission.add_default_permissions()

    roles = Role.query.all()
    permissions = Permissions.query.all()


    return jsonify({"role": list([role.name for role in roles]), "permission": list([permission.name for permission in permissions])})

@admin.route("/register", methods=["GET", "POST"])
def register():
    # user = Users(
    #     username="admin", name="tambe hanslett", 
    #     email="admin", password=bcrypt.generate_password_hash("admin")
    # )

    user = Users.query.filter_by(username="admin").first()

    # user.role = Role.query.filter_by(name="superadmin").first()
    # Give this user 3 more permissions 
    perm1 = Permissions.query.filter_by(name="superadmin.create_admin").first()
    perm2 = Permissions.query.filter_by(name="create").first()
    perm3 = Permissions.query.filter_by(name="read").first()

    user.permissions.append(perm1)
    user.permissions.append(perm2)
    user.permissions.append(perm3)
    # db.session.add(user)
    db.session.commit()

    return jsonify({"users": user.role.name})