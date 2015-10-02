from models import db
from models.news import News
from models.comment import Comment

class User(db.Model):

    __tablename__ = 'tbl_user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), unique=True)
    passwd = db.Column(db.String(32))
    salt = db.Column(db.String(32))
    nickname = db.Column(db.String(32))
    register_time = db.Column(db.DateTime)
    gender = db.Column(db.Integer)
    birthday = db.Column(db.DateTime)
    avatar_url = db.Column(db.String(4096))
    newses = db.relationship('News', backref='author', lazy='dynamic')
    comments = db.relationship('Comment', backref='author', lazy='dynamic')

    def __init__(self, username, passwd, salt, nickname, register_time, 
                 gender, birthday, avatar_url):
        self.username = username
        self.passwd = passwd
        self.salt = salt
        self.nickname = nickname
        self.register_time = register_time
        self.gender = gender
        self.birthday = birthday
        self.avatar_url = avatar_url

    def __repr__(self):
        return '<User %r>' % self.username

