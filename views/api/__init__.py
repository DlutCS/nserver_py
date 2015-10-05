# -*- coding: utf-8 -*-

from flask import Blueprint, url_for, redirect
from flask import request
from flask import make_response
from functools import wraps
from flask import jsonify, abort
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
            if not isinstance(r, tuple): # a normal Response
                return r
            res = {}
            if len(r) > 0:
                res['code'] = r[0]
            if len(r) > 1:
                res['msg'] = r[1]
            if len(r) > 2:
                res['data'] = r[2]
            res = jsonify(res)
            return allow_cross_domain(res)
        endpoint = options.pop('endpoint', func.__name__)
        if cache.get(endpoint, None) is not None:
            endpoint += rule
        cache[endpoint] = 1
        api.add_url_rule(rule, endpoint, wrapper, **options)
        return wrapper
    return _

@restful('/')
def index():
    # abort(404)
    return 200, 'this is index', 'data'

@restful('/category')
def get_categorys():
    categorys = Category.get_all()
    if not categorys:
        return 10001, 'empty'
    return 200, 'get categorys ok', categorys

@restful('/news/<id>')
def get_news(id):
    if id.isdigit():
        news = News.get(id)
    else:
        news = News.get_by_alias(id)
    if news:
        return 200,'', news
    return 404, 'news id not found'

@restful('/news/')
@restful('/news/latest/')
def news_latest():
    data = {}
    start = request.args.get('start', 0)
    rs = News.get_all('create_time', int(start));
    data['count'] = len(rs) if rs else 0
    data['news.list'] = rs
    return 200, 'get latest news ok', data

@restful('/news/popular')
def news_popular():
    data = {}
    start = request.args.get('start', 0)
    rs = News.get_all('comment_count', int(start));
    if not rs:
        return 10001, 'empty'
    data['count'] = len(rs)
    data['news.list'] = rs
    return 200, 'get popular news ok', data

@restful('/news/category/<int:cid>/latest')
def news_by_category_latest(cid):
    data = {}
    start = request.args.get('start', 0)
    rs = News.get_by_category(cid, 'create_time', int(start))
    data['count'] = len(rs)
    data['News.list'] = rs
    return 200, 'get latest category news ok', data

@restful('/news/category/<int:cid>')
@restful('/news/category/<int:cid>/popular')
def news_by_category_popular(cid):
    data = {}
    start = request.args.get('start', 0)
    rs = News.get_by_category(cid, 'comment_count', int(start))
    data['count'] = len(rs)
    data['News.list'] = rs
    return 200, 'get popular category news ok', data

# special 404
@restful("/<path:invalid_path>")
def not_found(invalid_path):
    return 404, "There isn't anything at: " + invalid_path



