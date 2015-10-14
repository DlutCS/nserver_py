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

    @classmethod
    def delete(cls, id):
        sql = 'delete from {} where id=%s'.format(cls.__table__)
        params = (id,)
        state = False
        try:
            store.execute(sql, params)
            store.commit()
            state = True
        except e:
            print "Error", e.args[0], e.args[1]
            store.rollback()
        return state







