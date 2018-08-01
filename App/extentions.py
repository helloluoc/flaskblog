from flask.ext.bootstrap import Bootstrap
from flask.ext.login import LoginManager
from flask.ext.mail import Mail
from flask.ext.migrate import Migrate
from flask.ext.moment import Moment
from flask.ext.uploads import UploadSet,IMAGES, configure_uploads
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate(db=db)
bs = Bootstrap()
mail = Mail()
lm = LoginManager()
photos = UploadSet('photos', IMAGES)
moment = Moment()

def init_extentions(app):
    db.init_app(app)
    migrate.init_app(app)
    bs.init_app(app)
    mail.init_app(app)
    configure_uploads(app, photos)
    moment.init_app(app)

    lm.init_app(app)
    lm.login_view = 'userbp.login'
    lm.login_message = 'login required!'
    lm.session_protection = 'strong'