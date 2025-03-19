# Utils.py file - Handles external functions that reside in the routes

from rondo.defaults import ROUTE_PATHS
from rondo.extensions import db
from rondo.models.roles_permissions import Permissions
from rondo.models.users import Users


def get_permission_objects(perm_list: list) -> list:
    permissions = []
    for permission in perm_list:
        x = db.session.execute(
            db.select(Permissions).filter_by(name=permission.lower())
        ).first()
        permissions.append(x)
    return permissions


def get_user_route(user: Users):
    role = user.role.name
    return ROUTE_PATHS[role]
