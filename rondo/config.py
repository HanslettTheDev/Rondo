import os

class Config:
    DEBUG = os.getenv("DEBUG")
    SECRET_KEY = os.getenv("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # MAIL_SERVER = os.getenv("MAIL_SERVER")
    # MAIL_PORT = os.getenv("MAIL_PORT")
    # MAIL_USE_TLS = os.getenv("MAIL_USE_TLS")
    # TESTING = os.getenv("TESTING")
    # MAIL_USERNAME = os.getenv("MAIL_USERNAME")
    # MAIL_DEFAULT_SENDER = os.getenv("MAIL_DEFAULT_SENDER")
    # MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")