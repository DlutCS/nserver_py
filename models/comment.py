# -*- coding: utf-8 -*-

from models import Model, store

class Comment(Model):

    __table__ = 'tbl_comment'

    def __init__(self, title, content, create_time, news_id, author_id):
        self.title = title
        self.content = content
        self.create_time = create_time
        self.news_id = news_id
        self.author_id = author_id

    def __repr__(self):
        return '<Comment %r>' % self.title

