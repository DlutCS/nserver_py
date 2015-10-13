# -*- coding: utf-8 -*-

from models import Model, store
from utils.consts import now

class Comment(Model):

    __table__ = 'tbl_comment'

    def __init__(self, content, create_time, news_id, author_id):
        self.content = content
        self.create_time = create_time
        self.news_id = news_id
        self.author_id = author_id

    def __repr__(self):
        return '<Comment %r>' % self.content

    @classmethod
    def create(cls, content, news_id, author_id):
        sql = '''insert into {}(content, news_id, author_id, create_time)
                 values(%s, %s, %s, %s)
              '''.format(cls.__table__)
        params = (content, news_id, author_id, now())
        try:
            store.execute(sql, params)
            _id = store.commit()
        except e:
            print "Error", e.args[0], e.args[1]
            store.rollback()
        return cls.get(_id) if _id else None


