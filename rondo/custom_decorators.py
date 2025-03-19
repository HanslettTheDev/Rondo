from functools import wraps

from flask import flash, redirect, request, url_for
from flask_login import current_user, logout_user

from rondo.auth.utils import get_user_route
from rondo.user.utils import get_permission_strings


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
                return redirect(url_for("auth.login", next=request.url))
            # check the users role and see if it matches the others
            if current_user.role.name.lower() not in roles:
                flash("Sorry, you do not have the access rights to that page", "error")
                return redirect(url_for(get_user_route(current_user)))

            # return the route function if all the conditions above pass
            return fn(*args, **kwargs)

        return decorated_view

    return wrapper


def is_approved():
    """
    Checks if a user accounts profile has been approved
    """

    def wrapper(fn):
        @wraps(fn)
        def decorated_view(*args, **kwargs):
            if "pending" in get_permission_strings(current_user.permissions):
                return redirect(url_for("user.not_active"))
            return fn(*args, **kwargs)

        return decorated_view

    return wrapper
