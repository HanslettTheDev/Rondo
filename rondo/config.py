import os
from rondo.utils import get_env


class Config:
    DEBUG = get_env("DEBUG")
    SECRET_KEY = get_env("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = get_env("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = get_env("SQLALCHEMY_TRACK_MODIFICATIONS")
    MAIL_SERVER = get_env("MAIL_SERVER")
    MAIL_PORT = get_env("MAIL_PORT")
    MAIL_USE_TLS = get_env("MAIL_USE_TLS")
    TESTING = get_env("TESTING")
    MAIL_USERNAME = get_env("MAIL_USERNAME")
    MAIL_DEFAULT_SENDER = get_env("MAIL_DEFAULT_SENDER")
    MAIL_PASSWORD = get_env("MAIL_PASSWORD")