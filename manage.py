from flask import Flask
from flask_script import Manager

from App.config import create_app
from App.extentions import db

app = Flask(__name__)
create_app(app)
manage = Manager(app)

@manage.command
def createDb():
    db.create_all()

#manage.add_command("db",MigrateCommand)

if __name__ == '__main__':
    manage.run()
