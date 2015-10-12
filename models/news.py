# -*- coding: utf-8 -*-

from models import Model, store
from models.category import Category
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
        return self.content[:MAX_SHORT_CONTENT]

    @property
    def category(self):
        return Category.get(self.category_id).name

    @classmethod
    def get_all(cls, order, start=0, limit=PAGE_LIMIT):
        sql = 'select * from {} order by %s desc limit %s,%s'.format(cls.__table__)
        params = (order, start, limit)
        rs = store.execute(sql, params)
        return [cls(**r).ldict() for r in rs] if rs else []

    @classmethod
    def get_by_category(cls, cid, order, start=0, limit=PAGE_LIMIT):
        sql = 'select * from {} where category_id=%s order by %s desc limit %s,%s'.format(cls.__table__)
        params = (cid, order, start, limit)
        rs = store.execute(sql, params)
        return [cls(**r).ldict() for r in rs] if rs else []

    @classmethod
    def get_by_alias(cls, alias):
        sql = 'select * from {} where alias_title=%s'.format(cls.__table__)
        params = (alias, )
        rs = store.execute(sql, params)
        return cls(**rs[0]) if rs else None

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
            'create_time':self.create_time
        }



