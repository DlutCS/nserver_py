# -*- coding: utf-8 -*-

from flask.ext.mysqldb import MySQL

mysql = MySQL()

class Store():
    def execute(self, sql, args):
        cur = mysql.connection.cursor()
        cur.execute(sql, args)
        rows = cur.fetchall()
        return rows

    def commit(self):
        mysql.connection.commit()

    def rollback(self):
        mysql.connection.rollback()


_clients = {}
key = 'MYSQL_DB'
def get_store():
    client = _clients.get(key, None)
    if client is None:
        client = Store()
        _clients[key] = client
    return client

store = get_store()

class Model(object):

    __table__ = ''

    @classmethod
    def get(cls, id):
        sql = 'select * from {} where id=%s'.format(cls.__table__)
        params = (id,)
        rs = store.execute(sql, params)
        return cls(**rs[0]) if rs else None





