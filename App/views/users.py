from flask import Blueprint
from flask import redirect
from flask import render_template
from flask import url_for
from flask_login import login_user,logout_user
from flask_mail import Message
from wtforms import form

from App.extentions import db
from App.views.forms import registerForm, loginForm

userbp = Blueprint("userbp", __name__)
from App.models.user import User

@userbp.route("/",methods=["GET","POST"])
def showfirst():
    return render_template("app/user/longin.html")

@userbp.route("/sendmail")
def sendmail():
    msg = Message("hello",sender="1636796608@qq.com",
                  recipients="1636796608@qq.com")
    msg.send()

@userbp.route("/register",methods=["GET","POST"])
def userRegister():
    db.create_all()
    register = registerForm()
    if register.validate_on_submit():
        username = register.name.data
        password = register.password.data
        email = register.email.data
        print(username,password,email)

        userInfo = User(username=username,password=password,email=email)
        db.session.add(userInfo)
        return "注册成功"
    return render_template("app/user/register.html", form=register)

@userbp.route("/login", methods=["GET","POST"])
def login():
    form = loginForm()
    if form.validate_on_submit():
        username = form.name.data
        password = form.password.data
        renember = form.submit.data


        u = User.query.filter(User.username==username,User.password==password).first()
        if u:
            login_user(u, remember=renember)
            print("登录成功")
            return redirect(url_for("main.hello_world"))
        else:
            return redirect(url_for("userbp.login"))
    return render_template("app/user/longin.html", form=form)

@userbp.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("main.hello_world"))