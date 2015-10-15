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
        except:
            store.rollback()
        return state

    @classmethod
    def update(cls, id, keys, values):
        keyformat = '=%s,'.join(keys) + '=%s'
        sql = 'update {} set {} where id=%s'.format(cls.__table__, keyformat)
        values.append(int(id))
        params = tuple(values)
        rcnt = 0
        print sql % params
        try:
            rcnt = store.execute(sql, params, True)
            store.commit()
        except:
            print 'except:', sql % params
            store.rollback()
        print 'rcnt=', rcnt
        return cls.get(id) if rcnt > 0 else None







