from flask import Blueprint, flash, jsonify, redirect, render_template, request, url_for
from flask_login import current_user, login_required
from rondo.defaults import DEFAULT_ROLE_PERMISSIONS
from rondo.extensions import db, bcrypt
from rondo.models.users import Users
from rondo.models.roles_permissions import Role, UserPermissions, UserRoles, Permissions
from rondo.models.logs import Logs
from rondo.models.laptop import LaptopTable, laptopIventory
from rondo.wrappers import role_required
from rondo.superadmin.utils import delete_previous_permissions, get_permission_objects, check_permission

user = Blueprint("admin", __name__)

@user.route('/dashboard')
@login_required
def dashboard():
    return render_template("user/main.html", title="Dashboard")

