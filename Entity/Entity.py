from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://lfuxpjslxdskzz:2d344d058bf11dc9b96f033972818cf5e16866131abb0b5d169e6f190d691b14@ec2-54-83-23-91.compute-1.amazonaws.com:5432/d4h44vei3vjngp'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


class PictureDate(db.Model):
    __tablename__ = 'PictureDate'

    Id = db.Column(db.Integer, primary_key=True)
    Uuid = db.Column(db.String(64), unique=True)
    Title = db.Column(db.String(64))
    Description = db.Column(db.String(128))

class LEARN_WORD(db.Model):
    __tablename__ = 'LEARN_WORD'

    KEYWORD = db.Column(db.String(200), primary_key=True)
    MESSAGE = db.Column(db.String(200))

if __name__ == '__main__':
    manager.run()