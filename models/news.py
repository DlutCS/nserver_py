# -*- coding: utf-8 -*-

from models import Model, store
from models.category import Category
from utils.memcache import memcache
import random
from utils.consts import *


class News(Model):

    __table__ = 'tbl_news'


    def __init__(self, id, title, alias_title, content, create_time, comment_count, read_count,
                 like_count, dislike_count, cover_url, category_id, author_id):
        self.id = id
        self.title = title
        self.alias_title = alias_title
        self.content = content
        self.create_time = create_time
        self.comment_count = comment_count
        self.read_count = read_count
        self.like_count = like_count
        self.dislike_count = dislike_count
        self.cover_url = cover_url
        self.category_id = category_id
        self.author_id = author_id

    @property
    def content_short(self):
        import re
        htmlStruct = re.compile(r'<[^>]+>')
        return htmlStruct.sub('',self.content)[:MAX_SHORT_CONTENT]

    @property
    def category(self):
        return Category.get_dict()[self.category_id].name

    @property
    def author(self):
        from models.user import User
        return User.get_dict()[self.author_id].nickname

    @classmethod
    @memcache("nserver:news_all[<order>,<start>,<limit>]")
    def get_all(cls, order, start=0, limit=PAGE_LIMIT):
        sql = 'select * from {} order by {} limit %s,%s'.format(cls.__table__, order)
        params = (start, limit)
        rs = store.execute(sql, params)
        return [cls(**r).ldict() for r in rs] if rs else []

    @classmethod
    def get_dict(cls, order, start=0, limit=PAGE_LIMIT):
        values = cls.get_all(order=order, start=start, limit=limit)
        keys = [ item.ldict()['id'] for item in values ]
        return dict(zip(keys,values))

    @classmethod
    @memcache("nserver:news_category[<cid>,<order>,<start>,<limit>]")
    def get_by_category(cls, cid, order, start=0, limit=PAGE_LIMIT):
        sql = 'select * from {} where category_id=%s order by {} limit %s,%s'.format(cls.__table__, order)
        params = (cid, start, limit)
        rs = store.execute(sql, params)
        return [cls(**r).ldict() for r in rs] if rs else []

    @classmethod
    def get(cls, nid):
        sql = 'select * from {} where id=%s'.format(cls.__table__)
        params = (nid, )
        rs = store.execute(sql, params)
        return cls(**rs[0]) if rs else None

    @classmethod
    @memcache("nserver:news[<alias>]")
    def get_by_alias(cls, alias):
        sql = 'select * from {} where alias_title=%s'.format(cls.__table__)
        params = (alias, )
        rs = store.execute(sql, params)
        return cls(**rs[0]) if rs else None

    @classmethod
    def random(cls):
        sql = ''''update tbl_news set read_count=read_count+1 where id=ceil({}*RAND());'''.format(self.get_total()+1000)
        rs = store.execute(sql)
        return True

    @classmethod
    def get_total(cls):
        sql = '''select count(*) as total from {}'''.format(cls.__table__)
        rs  = store.execute(sql)
        return rs[0]['total']

    @classmethod
    @memcache(clear=True)
    def create(cls, title, content, cover_url, category_id, author_id,  alias_title=None):
        sql = '''insert into {}(title, alias_title, content, cover_url, category_id, author_id, create_time)
                values(%s, %s, %s, %s, %s, %s, %s)
            '''.format(cls.__table__)
        params = (title, alias_title, content, cover_url, category_id, author_id, now())
        try:
            store.execute(sql, params)
            _id = store.commit()
        except e:
            print "Error", e.args[0], e.args[1]
            store.rollback()
        print _id
        return cls.get(id=_id) if _id else None

    def ldict(self):
        return {
            'id': self.id,
            'title': self.title,
            'alias_title': self.alias_title,
            'content_short':self.content_short,
            'read_count':self.read_count,
            'like_count':self.like_count,
            'dislike_count':self.dislike_count,
            'cover_url':self.cover_url,
            'category_id':self.category_id,
            'category':self.category,
            'author_id':self.author_id,
            'create_time':self.create_time,
            'author': self.author
        }

    @classmethod
    @memcache("nserver:news[<id>]")
    def get(cls, id):
        return super(News, cls).get(id=id)



