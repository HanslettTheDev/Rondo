from rondo.extensions import db
from rondo.models.users import Users
from rondo.defaults import DEFAULT_ROLES
from rondo.defaults import DEFAULT_PERMISSIONS

class Permissions(db.Model):
    __tablename__ = "permissions"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(255), nullable=True)

    def __repr__(self):
        return '<Permission %r>' % self.name
    
    @staticmethod
    def add_default_permissions():
        for permission in DEFAULT_PERMISSIONS:
            db.session.add(Permissions(name=permission))
            db.session.commit()


class Role(db.Model):
    __tablename__ = "roles"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(255), nullable=True)

    def __repr__(self):
        return '<Role %r>' % self.name
    
    @staticmethod
    def get_by_name(name):
        return Role.query.filter_by(name=name).first()
    
    @staticmethod
    def add_default_roles():
        for role in DEFAULT_ROLES:
            db.session.add(Role(name=role))
            db.session.commit()
           

class UserRoles(db.Model):
    __tablename__ = "user_roles"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id", ondelete="CASCADE"))
    role_id = db.Column(db.Integer, db.ForeignKey("roles.id", ondelete="CASCADE")) 

class UserPermissions(db.Model):
    __tablename__ = "user_permissions"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id", ondelete="CASCADE"))
    permission_id = db.Column(db.Integer, db.ForeignKey("permissions.id", ondelete="CASCADE"))   