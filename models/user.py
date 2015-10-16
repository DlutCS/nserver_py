# -*- coding: utf-8 -*-

from models import Model
from models.news import News
from models.comment import Comment
from models import store
from utils.consts import now
import md5
import random, string
import datetime

class User(Model):

    __table__ = 'tbl_user'

    def __init__(self, id, username, passwd, salt, nickname, register_time, 
                 gender, birthday, avatar_url, group_id):
        self.id = id
        self.username = username
        self.passwd = passwd
        self.salt = salt
        self.nickname = nickname
        self.register_time = register_time
        self.gender = gender
        self.birthday = birthday
        self.avatar_url = avatar_url
        self.group_id = group_id

    def __repr__(self):
        return '<User %r>' % self.username

    @classmethod
    def get_all(cls, start, limit):
        sql = 'select * from {} limit %s,%s'.format(cls.__table__)
        params = (start, limit)
        rs = store.execute(sql, params)
        return [cls(**r) for r in rs] if rs else None
        

    #----for authertic
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2
        except NameError:
            return str(self.id)  # python 3

    def get_auth_token(self):
        return unicode(self.passwd)

    @classmethod
    def get_by_token(cls, token):
        sql = 'select * from {} where passwd=%s'.format(cls.__table__)
        params = (token, )
        rs = store.execute(sql, params)
        return cls(**rs[0]) if rs else None

    @classmethod
    def get_total(cls):
        sql = '''select count(*) as total from {}'''.format(cls.__table__)
        rs  = store.execute(sql)
        return rs[0]['total']

    #----end auth
    
    @classmethod
    def validate(cls, username, passwd):
        rs = store.execute('select salt from {} where username=%s'.format(cls.__table__), (username,))
        salt = rs[0]['salt'] if rs else None
        if not salt:
            return None
        print '##salt=' , salt
        passwd = md5.new(passwd+salt).hexdigest()
        sql = 'select * from {} where username=%s and passwd=%s'.format(cls.__table__)
        params = (username, passwd)
        rs = store.execute(sql, params)
        return cls(**rs[0]) if rs else None

    @classmethod
    def create(cls, username, passwd, nickname, gender, birthday, avatar_url):
        salt = ''.join(random.sample(string.ascii_letters, 6))
        passwd = md5.new(passwd + salt).hexdigest()
        sql = '''insert into {}(username, passwd, nickname, salt, gender, birthday, avatar_url, register_time) 
                 values(%s, %s ,%s, %s, %s, %s, %s, %s)'''.format(cls.__table__)
        params = (username, passwd, nickname, salt, gender, birthday, avatar_url, now())
        try:
            store.execute(sql, params)
            _id = store.commit()
        except e:
            print "Error", e.args[0], e.args[1]
            store.rollback()
        print _id
        return cls.get(_id) if _id else None

    @classmethod
    def get_by_username(cls, username):
        sql = 'select * from {} where username=%s'.format(cls.__table__)
        params = (username,)
        rs = store.execute(sql, params)
        return cls(**rs[0]) if rs else None


    def dict(self):
        return {
            'id':self.id,
            'username':self.username,
            'nickname':self.nickname,
            'gender':self.gender,
            'birthday':self.birthday,
            'avatar_url':self.avatar_url,
            'group_id':self.group_id,
            # 'token':self.get_auth_token()
        }





