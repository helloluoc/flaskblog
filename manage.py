from flask.ext.migrate import MigrateCommand
from flask.ext.script import Manager
from app import create_app
from app.extentions import db

app = create_app()
manager = Manager(app)
manager.add_command('db', MigrateCommand)

@manager.command
def createdb():
    db.create_all()

if __name__ == '__main__':
    manager.run()
