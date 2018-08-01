from flask import current_app
from flask.ext.login import UserMixin

from app import db
from itsdangerous import TimedJSONWebSignatureSerializer as JWS

from app.extentions import lm


class User(UserMixin,db.Model):
    __tablename__='user'

    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(20),nullable=False,unique=True)
    password = db.Column(db.String(200),nullable=False)
    email = db.Column(db.String(100),nullable=False,unique=True)
    confirmed = db.Column(db.Boolean,default=False)
    icon = db.Column(db.String(32),default='monkey.jpg')

    posts = db.relationship('Post',backref='user',lazy='dynamic')
    collections = db.relationship('Post',backref=db.backref('users',lazy='dynamic'),lazy='dynamic',secondary='collection')

    def generate_token(self):
        jws = JWS(current_app.config['SECRET_KEY'],expires_in=3600)
        token = jws.dumps({'id':self.id})
        return token.decode()

    def is_collected(self,pid):
        for p in self.collections:
            print("is_collected:",pid,p.id)
            if p.id == pid:
                return True

        return False

    @staticmethod
    def check_token(token):
        jws = JWS(current_app.config['SECRET_KEY'])

        try:
            data = jws.loads(token)
        except Exception:
            return False

        uid =  data.get('id')
        print('check_token,uid=',uid)
        user = User.query.get(uid)

        if user:
            user.confirmed = True
            db.session.add(user)
            return True
        else:
            return False

@lm.user_loader
def get_user(uid):
    return User.query.get(uid)