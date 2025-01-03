from rondo import db
from rondo.models.roles_permissions import RolesAssigned, PermissionsAssigned


class Users(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    has_role = db.Column(db.Boolean, nullable=False, default=False)
    role_assigned_id = db.relationship("RolesAssigned", backref="role_assigned", lazy=True)
    permissions_assigned = db.relationship("PermissionsAssigned", backref="permission_assigned", lazy=True)

    def __repr__(self):
        return '<User %r>' % self.username