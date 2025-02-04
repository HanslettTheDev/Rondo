import os
import sys
from flask import Flask 
from rondo.extensions import db, login_manager, migrate, bcrypt
from rondo.config import Config



def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    bcrypt.init_app(app)
    # mail.init_app(app)

    from rondo.auth.routes import auth
    from rondo.superadmin.routes import superadmin


    app.register_blueprint(superadmin)
    app.register_blueprint(auth)

    return app
