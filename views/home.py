# -*- coding: utf-8 -*-

from flask.views import MethodView
from flask import redirect, render_template, request
from models.category import Category
from models.news import News



class HomeView(MethodView):

    def get(self):
        categories = Category.get_all();
        news_header = News.get_random(4)
        news_hot = News.get_all("create_time", start=0)
        return render_template('index.html',**locals())
