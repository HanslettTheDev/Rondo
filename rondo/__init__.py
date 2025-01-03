import os
from functools import wraps
from flask import Flask, flash, redirect, request, url_for
from flask_login import current_user, logout_user
from rondo.extensions import db, login_manager, migrate, bcrypt
from rondo.config import Config
# from rondo._config import get_config

path = os.path.join(
    os.path.abspath(os.path.dirname(__file__)),
    "db.sqlite"
)



def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    # login_manager.init_app(app)
    # bcrypt.init_app(app)
    # mail.init_app(app)

    from rondo.admin.routes import admin
    app.register_blueprint(admin)

    return app