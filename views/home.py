# -*- coding: utf-8 -*-

from flask.views import MethodView
from flask import redirect, render_template, request
from models.category import Category
from models.news import News
from models.forms import LoginForm, RegisterForm
from flask import abort, url_for



class HomeView(MethodView):

    def get(self):
        cid = 1
        news_header = News.get_all(order='create_time desc', start=0, limit=7)
        news_latest = News.get_all(order='create_time desc', start=7)
        news_popular = News.get_all(order='read_count desc', start=0)
        loginform = LoginForm()
        regform = RegisterForm()
        return render_template('index.html', **locals())


class HomeCategoryView(MethodView):

    def get(self, cid):
        if not cid or not Category.get(cid):
            abort(404)
        if cid == 1:
            return redirect(url_for('main.home'))
        news_header = News.get_by_category(cid=cid, order='create_time desc', start=0, limit=7)
        news_latest = News.get_by_category(cid=cid, order='create_time desc', start=7)
        news_popular = News.get_by_category(cid=cid, order='read_count desc', start=0)
        loginform = LoginForm()
        regform = RegisterForm()
        return render_template('index.html', **locals())


class HomeNewsView(MethodView):

    def get(self, nid):
        news = None
        if not nid:
            abort(404)

        news = News.get(id=nid) or News.get_by_alias(alias=nid)
        if not news:
            abort(404)

        news.update(news.id, 'read_count', news.read_count+1)
        loginform = LoginForm()
        regform = RegisterForm()
        news_popular = News.get_all(order='id', start=0)
        
        return render_template('news.html', **locals())
