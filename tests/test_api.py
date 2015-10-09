# -*- coding: utf-8 -*-

import unittest
from app import app

class ApiTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_index(self):
        assert self.app.get('/api/').status_code == 500
        assert self.app.get('/api').status_code == 301

    def test_category(self):
        assert self.app.get('/api/category/').status_code == 200
        assert self.app.get('/api/category').status_code == 301
        assert self.app.get('/api/categorys/').status_code == 500

    def test_news(self):
        assert self.app.get('/api/news/1/').status_code == 200
        assert self.app.get('/api/news/1000/').status_code == 500
        assert self.app.get('/api/news/nasa-water/').status_code == 200

    def test_newslist_latest(self):
        assert self.app.get('/api/newslist/').status_code == 200
        assert self.app.get('/api/newslist/latest').status_code == 301

    def test_newslist_popular(self):
        assert self.app.get('/api/newslist/popular/').status_code == 200

    def test_newslist_latest_with_category(self):
        assert self.app.get('/api/newslist/category/1/').status_code == 200
        assert self.app.get('/api/newslist/category/1000/').status_code == 200
        assert self.app.get('/api/newslist/category/1/latest/').status_code == 200
        assert self.app.get('/api/newslist/category/1000/latest/').status_code == 200

    def test_newslist_popular_with_category(self):
        assert self.app.get('/api/newslist/category/1/popular/').status_code == 200
        assert self.app.get('/api/newslist/category/1000/popular/').status_code == 200

    def test_not_found(self):
        assert self.app.get('/api/asfdasdfasd/asdf/').status_code == 500
        assert self.app.get('/api/asfdasdf').status_code == 301




