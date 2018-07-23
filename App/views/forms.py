from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, StringField, BooleanField
from wtforms.validators import  Required, DataRequired, Length


class PostForm(FlaskForm):
    content = TextAreaField(render_kw={"placeholder":"憨批你想说什么啊"},
                            validators=[DataRequired('NOT NONE'),
                            Length(min=5,max=250,message="between 5-250"),

    ])
    submit = SubmitField(label="submit")

class registerForm(FlaskForm):
    name = StringField(label="姓名",
                       render_kw={"placehloder":"输入姓名"},
                       validators=[
                        DataRequired("姓名不能为空"),
    ])
    password = StringField(label="密码",
                           render_kw={"placeholder":"输入密码"},
                           validators=[
                               DataRequired("密码不能为空")
    ])
    commit = StringField(label="确认密码",
                         render_kw={"placeholder":"确认密码"},
                         validators=[
                             DataRequired("憨批")
                         ])
    email = StringField(label="邮箱",
                        render_kw={"placeholder":"输入邮箱地址"})
    submit = SubmitField(label="提交")

class loginForm(FlaskForm):
    name = StringField(label="姓名",
                       render_kw={"placehloder":"输入姓名"},
                       validators=[
                        DataRequired("姓名不能为空"),
                       ])
    password = StringField(label="密码",
                           render_kw={"placeholder": "输入密码"},
                           validators=[
                               DataRequired("密码不能为空")
                           ])
    commit = StringField(label="确认密码",
                         render_kw={"placeholder": "确认密码"},
                         validators=[
                             DataRequired("憨批")
                         ])
    remberMe = BooleanField(label="记住我")
    submit = SubmitField(label="提交")

class iconPost(FlaskForm):

