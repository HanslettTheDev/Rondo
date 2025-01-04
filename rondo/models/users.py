from flask_login import UserMixin
from rondo.extensions import db, login_manager


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))


class Users(db.Model, UserMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    role = db.relationship(
        "Role", secondary="user_roles", uselist=False, cascade="all"
    )    
    permissions = db.relationship(
        "Permissions", secondary="user_permissions", uselist=True, cascade="all"
    )    

    def __repr__(self):
        return '<User %r>' % self.username


# Circular imports
from rondo.models.roles_permissions import Role, Permissions