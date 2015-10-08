# -*- coding: utf-8 -*-

from models import store

class Model(object):

    __table__ = ''

    @classmethod
    def get(cls, id):
        sql = 'select * from {} where id=%s'.format(cls.__table__)
        params = (id,)
        rs = store.execute(sql, params)
        return cls(**rs[0]) if rs else None




