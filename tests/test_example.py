#!-coding:utf8

import unittest
import app

class FlaskrTestCase(unittest.TestCase):

    def test_hello(self):
        print "hello"

    def test_world(self):
        print "world"

    def test_app(self):
        print app.hello_world()

