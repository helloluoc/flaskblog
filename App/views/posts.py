from flask import Blueprint,flash
from flask import redirect
from flask import url_for
from flask_login import login_required


postbp = Blueprint("postbp", __name__)

@postbp.route("/post")
@login_required
def postBlog():
    flash("发布成功")
    return redirect(url_for("main.hello_world"))