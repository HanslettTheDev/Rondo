from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
# from flask_mail import Mail

db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()
# mail = Mail()
login_manager = LoginManager()
login_manager.login_view = "must_login.login"
login_manager.login_message_category = "info"
