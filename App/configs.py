import os


class Config:
    SECRET_KEY = '123456'

    DATABASE_URI = 'sqlite:////home/sirouyang/MyBlog/db/blog.sqlite'
    SQLALCHEMY_DATABASE_URI = DATABASE_URI
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAX_CONTENT_LENGTH = 8 * 1024 * 1024

    # 需要配置绝对路径
    UPLOADED_PHOTOS_DEST = os.path.join(os.path.abspath(os.path.dirname(__file__)),'static','uploads')

    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'smtp.1000phone.com')
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME', 'ouyangsuo@1000phone.com')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD', '123456')



def init_configs(app):
    app.config.from_object(Config)


if __name__ == '__main__':
    print(os.path.abspath(os.path.dirname(__file__)))