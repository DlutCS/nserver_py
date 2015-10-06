# -*- coding: utf-8 -*-

from flask import Blueprint, url_for, redirect
from flask import request
from flask import Response
from flask import make_response
from functools import wraps
from flask import jsonify, abort
from flask import json
from models.news import News
from models.category import Category

api = Blueprint('api', __name__)

def allow_cross_domain(res):
    rst = make_response(res)
    rst.headers['Access-Control-Allow-Origin'] = '*'
    rst.headers['Access-Control-Allow-Methods'] = 'PUT,GET,POST,DELETE'
    allow_headers = "Referer,Accept,Origin,User-Agent"
    rst.headers['Access-Control-Allow-Headers'] = allow_headers
    return rst


def restful(rule, cache={}, **options):
    def _(func):
        @wraps(func)
        def wrapper(*a, **kw):
            r = func(*a, **kw)
            if isinstance(r, Response): # a normal Response
                return r
            res = json.dumps(r)
            return allow_cross_domain(res)
        endpoint = options.pop('endpoint', func.__name__)
        if cache.get(endpoint, None) is not None:
            endpoint += rule
        cache[endpoint] = 1
        api.add_url_rule(rule, endpoint, wrapper, **options)
        return wrapper
    return _

def error(code, msg):
    data = { "code": code, "msg": msg }
    res = allow_cross_domain(jsonify(data))
    return make_response(res, 500)

@restful('/')
def index():
    # abort(404)
    return error(10001, 'this is index, nothing here')

@restful('/category/')
def get_categorys():
    categorys = Category.get_all()
    if not categorys:
        return error(10002, 'empty')
    data = {}
    data['categorys'] = categorys
    data['total'] = len(categorys)
    return data

@restful('/news/<id>/')
def get_news(id):
    if id.isdigit():
        news = News.get(id)
    else:
        news = News.get_by_alias(id)
    if not news:
        return error(10003, 'news id not found')
    return news

@restful('/newslist/')
@restful('/newslist/latest/')
def news_latest():
    data = {}
    start = request.args.get('start', 0)
    rs = News.get_all('create_time', int(start));
    if not rs:
        return error(10001, 'empty')
    data['count'] = len(rs) if rs else 0
    data['news.list'] = rs
    return data

@restful('/newslist/popular/')
def news_popular():
    data = {}
    start = request.args.get('start', 0)
    rs = News.get_all('comment_count', int(start));
    if not rs:
        return 10001, 'empty'
    data['count'] = len(rs)
    data['newslist'] = rs
    return data

@restful('/newslist/category/<int:cid>/')
@restful('/newslist/category/<int:cid>/latest/')
def news_by_category_latest(cid):
    data = {}
    start = request.args.get('start', 0)
    rs = News.get_by_category(cid, 'create_time', int(start))
    if not rs:
        return error(10001, 'empty')
    data['count'] = len(rs)
    data['newslist'] = rs
    return data

@restful('/newslist/category/<int:cid>/')
@restful('/newslist/category/<int:cid>/popular/')
def news_by_category_popular(cid):
    data = {}
    start = request.args.get('start', 0)
    rs = News.get_by_category(cid, 'comment_count', int(start))
    if not rs:
        return error(10001, 'empty')
    data['count'] = len(rs)
    data['newslist'] = rs
    return data

# special 404
@restful("/<path:invalid_path>/")
def not_found(invalid_path):
    return error(404, "There isn't anything at: " + invalid_path)



