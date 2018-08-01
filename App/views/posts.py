from flask import Blueprint,flash,redirect,url_for, jsonify
from flask_login import login_required,current_user
from wtforms.ext import sqlalchemy

from app.models import Post

postbp = Blueprint('postbp', __name__)

@postbp.route('/showall/')
def showall():
    return 'showall'\

@postbp.route('/post/')
@login_required
def post():
    flash('发布成功！')
    return redirect(url_for('mainbp.index'))

@postbp.route('/switch_collect/<int:pid>/')
@login_required
def switch_collect(pid):
    post = Post.query.get(pid)

    if current_user.is_collected(pid):
        current_user.collections.remove(post)
        return jsonify({'result':False})
    else:
        current_user.collections.append(post)
        return jsonify({'result': True})



