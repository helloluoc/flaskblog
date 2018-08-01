from flask import Blueprint,render_template,redirect,url_for,flash,request
from app.extentions import db
from app.forms import PostForm
from app.models import User,Post
from flask_login import login_required,current_user


mainbp = Blueprint('mainbp', __name__)

@mainbp.route('/',methods=['GET','POST'])
def index():
    form = PostForm()

    if form.validate_on_submit():
        content = form.content.data
        user = current_user._get_current_object()
        post = Post(content=content,user=user)
        db.session.add(post)
        flash('发表成功！')

    # 展示所有内容
    page = int(request.args.get('page',1))
    pagination = Post.query.order_by(Post.posttime.desc()).paginate(page=page, per_page=5, error_out=False)
    posts = pagination.items

    return render_template('main/index.html',form=form,posts=posts,pagination=pagination,page=page)

@mainbp.route('/getmoney/')
@login_required
def getmoney():
    return '您可以免费在这里学习Python并到前台领取劳斯莱斯一辆'