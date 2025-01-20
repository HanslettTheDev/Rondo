# from flask import current_user, request
from functools import wraps
# from flask import flash, redirect, request, url_for
# from flask_login import current_user, logout_user

def role_required(role: str):
    def wrapper(fn):
        @wraps(fn)
        def decorated_view(*args, **kwargs):
            pass
        return decorated_view
    return wrapper
