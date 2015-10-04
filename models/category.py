# -*- coding: utf-8 -*-

from models import Model, store

class Category(Model):

    __table__ = 'tbl_category'

    def __init__(self, name):
        self.name = name
        
    def __repr__(self):
        return '<Category %r>' % self.name

