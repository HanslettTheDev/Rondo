from functools import wraps
from flask import flash, redirect, request, url_for
from flask_login import current_user, logout_user

def role_required(role: str | list):
    def wrapper(fn):
        @wraps(fn)
        def decorated_view(*args, **kwargs):
            roles = []
            if isinstance(role, str):
                roles.append(role.lower())
            elif isinstance(role, list):
                roles = role

            if not current_user.is_authenticated:
                flash("You must login first to view this route", "warning")
                return redirect(url_for('auth.login', next=request.url))
            # check the users role and see if it matches the others
            if current_user.role.name.lower() not in roles:
                flash("Sorry, you do not have the access rights to that page", "error")
                return redirect(url_for('superadmin.dashboard'))

            # return the route function if all the conditions above pass
            return fn(*args, **kwargs)
        return decorated_view
    return wrapper


# @admin.route("/fill")
# def fill():
#     role = Role()
#     role.add_default_roles()

#     permission = Permissions()
#     permission.add_default_permissions()

#     roles = Role.query.all()
#     permissions = Permissions.query.all()


#     return jsonify({"role": list([role.name for role in roles]), "permission": list([permission.name for permission in permissions])})

# @admin.route("/test", methods=["GET", "POST"])
# def register():
#     # user = Users(
#     #     username="admin", name="tambe hanslett", 
#     #     email="admin", password=bcrypt.generate_password_hash("admin")
#     # )

#     user = Users.query.filter_by(username="admin").first()

#     # user.role = Role.query.filter_by(name="superadmin").first()
#     # Give this user 3 more permissions 
#     perm1 = Permissions.query.filter_by(name="superadmin.create_admin").first()
#     perm2 = Permissions.query.filter_by(name="create").first()
#     perm3 = Permissions.query.filter_by(name="read").first()

#     user.permissions.append(perm1)
#     user.permissions.append(perm2)
#     user.permissions.append(perm3)
#     # db.session.add(user)
#     db.session.commit()

#     return jsonify({"users":  user.role.name})