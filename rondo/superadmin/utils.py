# Utils.py file - Handles external functions that reside in the routes
from rondo.extensions import db
from rondo.models.roles_permissions import Permissions, UserPermissions


def get_permission_objects(perm_list: list) -> list:
    permissions = []
    for permission in perm_list:
        x = db.session.execute(db.select(Permissions).filter_by(name=permission.lower())).first()
        permissions.append(x)
    return permissions


def check_permission(permissions: list, required_permission:str):
    permissions = [x.name for x in permissions]
    if required_permission in permissions:
        return True 
    return False


def delete_previous_permissions(user_id: int) -> bool:
    old_permissions = db.session.execute(db.select(UserPermissions).filter_by(user_id=user_id)).all()
    for perm in old_permissions:
        db.session.delete(perm[0])
        db.session.commit()
    return True