import os

from flask import Flask
from flask_mail import Mail

from App import config_blueprint, configErrorHandlers
from App.extentions import init_extentions


class Config:
    SECRET_KEY = "123456"

    databaseurl = "sqlite:///" + os.path.join(os.getcwd(), "db", "fuck.sqlite")
    SQLALCHEMY_DATABASE_URI = databaseurl
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER = "smtp.qq.com"
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = "1684798088@qq.com"
    MAIL_RECEIVER = "1636796608@qq.com"
    MAIL_PASSWORD = "lwoyahjoclrhedia"

def config_init(app):
    app.config.from_object(Config)

def create_app(app):
    #app = Flask(__name__)
    config_blueprint(app)
    configErrorHandlers(app)
    config_init(app)
    init_extentions(app)
    return app


