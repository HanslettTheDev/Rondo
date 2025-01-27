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
                flash("Sorry, you do not have the access rights to this page", "error")
                return redirect(url_for('admin.dashboard'))

            # return the route function if all the conditions above pass
            return fn(*args, **kwargs)
        return decorated_view
    return wrapper
