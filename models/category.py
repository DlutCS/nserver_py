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
        sql = 'select * from {} order by id asc'.format(cls.__table__)
        rs = store.execute(sql)
        return [cls(**r) for r in rs] if rs else []
        

    @classmethod
    @memcache('nserver:categories_dicts', 100)
    def get_dict(cls):
        values = cls.get_all()
        keys = [ item.dict()['id'] for item in values ]
        return dict(zip(keys,values))

    @classmethod
    @memcache(clear=True)
    def create(cls, name):
        sql = 'insert into {}(name) values(%s)'.format(cls.__table__)
        params = (name, )
        try:
            store.execute(sql, params)
            _id = store.commit()
        except e:
            print "Error", e.args[0], e.args[1]
            store.rollback()
        return cls.get(id=_id) if _id else None

    @classmethod
    @memcache(clear=True)
    def update(cls, id, name):
        sql = 'update {} set name=%s where id=%s'.format(cls.__table__)
        params = (name, id)
        try:
            store.execute(sql, params)
            _id = store.commit()
        except e:
            print "Error", e.args[0], e.args[1]
            store.rollback()
        return cls.get(id=_id) if _id else None

    def dict(self):
        return {
            'id':self.id,
            'name':self.name
        }





