#!-coding:utf8

import unittest
from app import app

class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_hello(self):
        print "hello"

    def test_world(self):
        print "world"

    def test_app(self):
        print self.client.get('/').data

    def test_login(self):
        print self.client.get('/login').data


