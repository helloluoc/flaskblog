from time import sleep

from flask import Blueprint, app
from flask import current_app
from flask import redirect
from flask import render_template
from flask import url_for
from flask_mail import Message

from App.extentions import db, mail
from App.views.forms import PostForm

mainbp = Blueprint("main", __name__)



@mainbp.route('/',methods=["GET","POST"])
def hello_world():
    renderForm = PostForm()
    if renderForm.validate_on_submit():
        return redirect(url_for("postbp.postBlog"))
    return render_template("app/main/index.html",form=renderForm)



@mainbp.route("/sendmail")
def sendMail():
    for i in range(10):
        msg = Message(
            subject="您好，上期开19你中了吗?+我薇:w573398728就有开奖晚上的一畄",
            recipients=["573398728@qq.com"],
            sender=current_app.config["MAIL_USERNAME"],
        )
        mail.send(msg)
        sleep(5)
    return "success to send a mail"