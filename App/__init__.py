from flask import Flask
from flask import render_template

from app.configs import init_configs
from app.extentions import db, init_extentions
from app.views import mainbp,postbp,userbp

blueprints = (
    (mainbp,''),
    (userbp,'/user'),
    (postbp,'/post')
)

def config_blueprints(app):
    for name,prefix in blueprints:
        app.register_blueprint(name, url_prefix=prefix)

def config_errorhandlers(app):
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('error/404.html')


def create_app():
    app = Flask(__name__)
    config_blueprints(app)
    config_errorhandlers(app)
    init_configs(app)
    init_extentions(app)

    return app