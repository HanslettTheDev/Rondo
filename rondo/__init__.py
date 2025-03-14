import os
import sys
from flask import Flask 
from rondo.extensions import db, login_manager, migrate, bcrypt
from rondo.config import Config
from rondo.commands import create, seed, superuser



def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    app.cli.add_command(create)
    app.cli.add_command(seed)
    app.cli.add_command(superuser)

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    bcrypt.init_app(app)
    # mail.init_app(app)

    from rondo.auth.routes import auth
    from rondo.superadmin.routes import superadmin
    from rondo.user.routes import user
    from rondo.errors.handlers import errors


    app.register_blueprint(superadmin)
    app.register_blueprint(auth)
    app.register_blueprint(errors)

    return app
