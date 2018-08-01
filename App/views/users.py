import threading

from flask import Blueprint, render_template,url_for,current_app,redirect,flash
from flask.ext.login import login_user,current_user,logout_user,login_required
from flask.ext.mail import Message
from app.extentions import mail, db, photos, lm
from app.forms import RegisterForm, LoginForm,UploadForm,ProfileForm
from app.models import User
from app.utils import sendmail

userbp = Blueprint('userbp', __name__)


@userbp.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        email = form.email.data
        print(username,password,email)

        user = User(username=username,password=password,email=email)
        db.session.add(user)
        db.session.commit()

        activate_url = url_for('userbp.activate',token=user.generate_token(),_external=True)
        print("activate_url=",activate_url)

        msg = Message(
            subject='please activate your email',
            recipients=[user.email],
            body='click <a href="'+activate_url+'">here</a> to acivate your email',
            html='click <a href="'+activate_url+'">here</a> to acivate your email',
            sender = current_app.config['MAIL_USERNAME']
        )
        threading.Thread(target=sendmail,args=(current_app._get_current_object(),msg)).start()

        return '注册成功！'
    return render_template('user/register.html', form=form)

@userbp.route('/activate/<token>')
def activate(token):
    if User.check_token(token):
        return '激活成功！'
    else:
        return '激活失败！'


@userbp.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        remember = form.remember.data
        print(username,password,remember)

        u = User.query.filter(User.username==username,User.password==password).first()
        if u:
            login_user(u, remember=remember)
            print('登录成功！',current_user._get_current_object().username)
            return redirect(url_for('mainbp.index'))
        else:
            return '查无此人！'

    return render_template('user/login.html', form=form)

@userbp.route('/logout/')
def logout():
    logout_user()
    return redirect(url_for('mainbp.index'))

@userbp.route('/upload_icon/', methods=['GET', 'POST'])
@login_required
def upload_icon():
    form = UploadForm()
    if form.validate_on_submit():
        file = form.file.data
        filepath = photos.save(file,name=file.filename)
        current_user.icon = file.filename

    url = photos.url(current_user.icon)
    return render_template('user/upload.html', form=form,imgurl=url)

@userbp.route('/profile/')
def profile():
    form = ProfileForm()
    form.username.data = current_user.username
    form.email.data = current_user.email
    return render_template('user/profile.html', form=form)
