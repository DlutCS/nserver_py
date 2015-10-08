# -*- coding: utf-8 -*-

from models import Model
from models.news import News
from models.comment import Comment
from models import store

class User(Model):

    __table__ = 'tbl_user'

    def __init__(self, id, username, passwd, salt, nickname, register_time, 
                 gender, birthday, avatar_url):
        self.id = id
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

    def update(self, username):
        sql = 'update {} set username=%s where id=%s'.format(self.__table__)
        params = (username, self.id)
        try:
            store.execute(sql, params)
            store.commit()
        except e:
            print "Error", e.args[0], e.args[1]
            store.rollback()



