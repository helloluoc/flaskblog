from flask import render_template

from App.views import mainbp,userbp,postbp

blueprint = (
    (mainbp,""),
    (userbp,"/userbp/"),
    (postbp,"/postbp"),
)
def config_blueprint(app):
    for name,prefix in blueprint:
        app.register_blueprint(name,url_prefix=prefix)

def configErrorHandlers(app):
    @app.errorhandler(404)
    def pageNotFound(e):
        return render_template("error/fourNoneFour.html")