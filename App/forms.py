from flask.ext.wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,PasswordField,BooleanField,FileField
from wtforms.validators import DataRequired,Length,EqualTo,Email


class PostForm(FlaskForm):
    content = TextAreaField(
        render_kw={'placeholder':'骚年，你想表达什么...'},
        validators=[
        DataRequired('stupid,data required!'),
        Length(min=5, max=200, message='stupid,length 2-200!')
    ])
    submit = SubmitField(label='发表')

class RegisterForm(FlaskForm):
    username = StringField(
        label='用户名',
        validators=[
            DataRequired('stupid,data required!'),
            Length(min=5, max=20, message='stupid,length 5-20!')
        ],
        render_kw={'placeholder':'please enter username'}
    )
    password = PasswordField(
        label='密码',
        validators=[
            DataRequired('stupid,data required!'),
            Length(min=5, max=20, message='stupid,length 5-20!')
        ],
        render_kw={'placeholder':'please enter password'}
    )
    repeat = PasswordField(
        label='确认密码',
        validators=[
            DataRequired('stupid,data required!'),
            EqualTo('password','stupid,not equal to the first')
        ],
        render_kw={'placeholder':'please enter password again'}
    )
    email = StringField(
        label='邮箱',
        validators=[
            DataRequired('stupid,data required!'),
            Length(min=5, max=100, message='stupid,length 5-20!'),
            Email('stupid,invalid email')
        ],
        render_kw={'placeholder':'please enter email'}
    )
    submit = SubmitField(label='注册')

class ProfileForm(FlaskForm):
    username = StringField(render_kw={'disabled':'disabled'})
    email = StringField(render_kw={'disabled':'disabled'})


class LoginForm(FlaskForm):
    username = StringField(
        label='用户名',
        validators=[
            DataRequired('stupid,data required!'),
            Length(min=5, max=20, message='stupid,length 5-20!')
        ],
        render_kw={'placeholder':'please enter username'}
    )
    password = PasswordField(
        label='密码',
        validators=[
            DataRequired('stupid,data required!'),
            Length(min=5, max=20, message='stupid,length 5-20!')
        ],
        render_kw={'placeholder':'please enter password'}
    )
    remember = BooleanField(label='记住我')

    submit = SubmitField(label='立即登录')

class UploadForm(FlaskForm):

    file = FileField(label='上传头像', validators=[
        DataRequired('stupid,data required!')
    ])

    submit = SubmitField(label='上传头像')
