# -*- coding: utf-8 -*-

from models import Model
from models.news import News
from models.comment import Comment


class User(Model):

    __table__ = 'tbl_user'

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

