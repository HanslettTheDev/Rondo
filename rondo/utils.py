from rondo.extensions import db
from rondo.models.roles_permissions import Permissions


def get_permission_objects(perm_list: list) -> list:
    permissions = []
    for permission in perm_list:
        x = db.session.execute(db.select(Permissions).filter_by(name=permission.lower())).first()
        permissions.append(x)
    return permissions
