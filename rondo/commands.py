import click
from flask.cli import with_appcontext

from rondo.defaults import DEFAULT_PERMISSIONS, DEFAULT_ROLE_PERMISSIONS, DEFAULT_ROLES
from rondo.extensions import bcrypt, db
from rondo.models.roles_permissions import Permissions, Role
from rondo.models.users import Users
from rondo.utils import get_permission_objects


@click.command(name="create")
@with_appcontext
def create():
    db.create_all()
    print("yeah")


@click.command(name="seed")
@with_appcontext
def seed():
    for permission in DEFAULT_PERMISSIONS:
        db.session.add(Permissions(name=permission))
        db.session.commit()
    print("Permissisons seeded", end="\n")

    for role in DEFAULT_ROLES:
        db.session.add(Role(name=role))
        db.session.commit()

    print("Roles seeded")


@click.command(name="superuser")
@with_appcontext
def superuser():
    user = Users(
        username="rondo",
        name="Rondo Admin",
        email="rondodefault@gmail.com",
        password=bcrypt.generate_password_hash("admin").decode("utf-8"),
    )

    role = db.session.execute(db.select(Role).filter_by(name="superadmin")).first()
    user.role = role[0]

    for permission in get_permission_objects(DEFAULT_ROLE_PERMISSIONS["superadmin"]):
        user.permissions.append(permission[0])

    db.session.add(user)
    db.session.commit()

