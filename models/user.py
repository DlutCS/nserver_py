# -*- coding: utf-8 -*-

from models import Model
from models.news import News
from models.comment import Comment
from models import store
import md5
import random, string

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

    @classmethod
    def validate(cls, username, passwd):
        rs = store.execute('select salt from {} where username=%s'.format(cls.__table__), (username,))
        print '##salt=' , salt
        if not rs:
            return None
        salt = rs[0]
        passwd = md5.new(passwd+salt).hexdigest()
        sql = 'select * from {} where username=%s and passwd=%s'.format(cls.__table__)
        params = (username, passwd)
        rs = store.execute(sql, params)
        return cls(**rs[0]) if rs else None

    @classmethod
    def create(cls, username, passwd, nickname, gender, birthday, avatar_url):
        salt = ''.join(random.sample(string.ascii_letters, 6))
        passwd = md5.new(passwd + salt).hexdigest()
        sql = '''insert into {}(username, passwd, nickname, gender, birthday, avatar_url)
                 values(%s, %s ,%s, %s, %s, %s)'''.format(cls.__table__)
        params = (username, passwd, nickname, gender, birthday, avatar_url)
        try:
            rs = store.execute(sql, params)
        except e:
            print "Error", e.args[0], e.args[1]
            store.rollback()
        return cls(**rs[0]) if rs else None

    @classmethod
    def get_by_username(cls, username):
        sql = 'select * from {} where username=%s'.format(cls.__table__)
        params = (username,)
        rs = store.execute(sql, params)
        return cls(**rs[0]) if rs else None





