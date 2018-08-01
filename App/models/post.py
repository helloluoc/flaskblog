from datetime import datetime

from app import db


class Post(db.Model):

    __tablename__='post'

    # ArgumentError:Mapper Mapping|Post|post could not assemble any primary key column for table 'post'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    content = db.Column(db.Text,nullable=False)
    posttime = db.Column(db.DateTime,default=datetime.utcnow)

    uid = db.Column(db.Integer,db.ForeignKey('user.id'))