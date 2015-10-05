# -*- coding: utf-8 -*-

from flask.views import MethodView
from flask import redirect, render_template, request
from models.category import Category
from models.news import News



class HomeView(MethodView):

    def get(self):
        return "hello,world"
