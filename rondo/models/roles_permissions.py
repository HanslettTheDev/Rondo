from rondo import db
from rondo.models.roles import Role
from rondo.models.permissions import Permissions
from rondo.models.users import Users

class RolesAssigned(db.Model):
    __tablename__ = "roles_assigned"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), ondelete="CASCADE")
    role_id = db.Column(db.Integer, db.ForeignKey("roles.id"), ondelete="CASCADE")  

class PermissionsAssigned(db.Model):
    __tablename__ = "permissions_assigned"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), ondelete="CASCADE")
    permission_id = db.Column(db.Integer, db.ForeignKey("permissions.id"), ondelete="CASCADE")   