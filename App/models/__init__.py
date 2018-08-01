from app.extentions import db
from app.models.post import Post
from app.models.user import User

collection = db.Table(
    'collection',
    db.Column('uid',db.Integer, db.ForeignKey('user.id')),
    db.Column('pid',db.Integer, db.ForeignKey('post.id'))
)

