from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
mail = Mail()
bs = Bootstrap()
lm = LoginManager()

def init_extentions(app):
    db.init_app(app)
    mail.init_app(app)
    bs.init_app(app)

    lm.init_app(app)
    lm.login_view = "userbp.login"
    lm.login_message = "login required"
    lm.session_protection = "strong"

