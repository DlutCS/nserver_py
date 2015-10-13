# -*- coding: utf-8 -*-

from models import Model, store
from utils.memcache import memcache

class Category(Model):

    __table__ = 'tbl_category'

    def __init__(self, id, name):
        self.id = id
        self.name = name
        
    def __repr__(self):
        return '<Category %r>' % self.name

    @classmethod
    @memcache('nserver:categories', 100)
    def get_all(cls):
        sql = 'select * from {}'.format(cls.__table__)
        rs = store.execute(sql)
        return [cls(**r) for r in rs] if rs else []
        
    @classmethod
    def create(cls, name):
        sql = 'insert into {}(name) values(%s)'.format(cls.__table__)
        params = (name, )
        try:
            store.execute(sql, params)
            _id = store.commit()
        except e:
            print "Error", e.args[0], e.args[1]
            store.rollback()
        return cls.get(_id) if _id else None







