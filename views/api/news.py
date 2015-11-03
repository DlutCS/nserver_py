# -*- coding: utf-8 -*-
from views.api import api, restful, error
from flask import request, render_template
from utils.consts import *
from models.news import News
from models.category import Category


@restful('/category/')
def get_categorys():
    data = {}
    categorys = Category.get_all()
    data['categories'] = categorys
    data['total'] = len(categorys)
    return data

@restful('/news/<id>/')
def get_news(id):
    if id.isdigit():
        news = News.get(id=id)
    else:
        news = News.get_by_alias(alias=id)
    if not news:
        return error(10003, 'news id not found')
    return news

@restful('/newslist/')
@restful('/newslist/latest/')
def news_latest():
    data = {}
    start = request.args.get('start', 0)
    limit = request.args.get('limit', PAGE_LIMIT)
    template  = request.args.get('template', False)
    rs = News.get_all(order='create_time desc', start=int(start), limit=int(limit));
    data['count'] = len(rs)
    

    if template:
        data['template'] = render_template('component/news_loop.html', data=rs)
    else:
        data['newslist'] = rs
    
    return data

@restful('/newslist/popular/')
def news_popular():
    data = {}
    start = request.args.get('start', 0)
    limit = request.args.get('limit', PAGE_LIMIT)
    rs = News.get_all(order='read_count desc', start=int(start), limit=int(limit));
    data['count'] = len(rs)
    data['newslist'] = rs
    return data

@restful('/newslist/category/<int:cid>/')
@restful('/newslist/category/<int:cid>/latest/')
def news_by_category_latest(cid):
    data = {}
    start = request.args.get('start', 0)
    limit = request.args.get('limit', PAGE_LIMIT)
    if cid == 1: # 头条内容
        rs = News.get_all(order='create_time desc', start=int(start), limit=int(limit))
    else:
        rs = News.get_by_category(cid=cid, order='create_time desc', start=int(start), limit=int(limit))
    data['count'] = len(rs)
    data['newslist'] = rs
    return data

@restful('/newslist/category/<int:cid>/')
@restful('/newslist/category/<int:cid>/popular/')
def news_by_category_popular(cid):
    data = {}
    start = request.args.get('start', 0)
    limit = request.args.get('limit', PAGE_LIMIT)
    rs = News.get_by_category(cid=cid, order='read_count desc', start=int(start), limit=int(limit))
    data['count'] = len(rs)
    data['newslist'] = rs
    return data

