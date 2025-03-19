from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required

from rondo.custom_decorators import is_approved, role_required

# from rondo.extensions import bcrypt, db
# from rondo.models.laptop import LaptopTable, laptopIventory
# from rondo.models.logs import Logs
# from rondo.models.roles_permissions import Permissions, Role, UserPermissions, UserRoles
# from rondo.models.users import Users

user = Blueprint("user", __name__, url_prefix="/user")


@user.route("/dashboard")
@login_required
@role_required("user")
@is_approved()
def dashboard():
    return render_template("user/main.html", title="Dashboard")


@user.route("/account_not_active")
@login_required
@role_required("user")
def not_active():
    return render_template("user/not_active.html")
