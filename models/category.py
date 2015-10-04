# -*- coding: utf-8 -*-

from models import Model, store

class Category(Model):

    __table__ = 'tbl_category'

    def __init__(self, id, name):
        self.id = id
        self.name = name
        
    def __repr__(self):
        return '<Category %r>' % self.name

    @classmethod
    def get_all(cls):
        sql = 'select * from {}'.format(cls.__table__)
        rs = store.execute(sql)
        return [cls(**r) for r in rs] if rs else None


