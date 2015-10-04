# -*- coding: utf-8 -*-

from flask import Blueprint, url_for, redirect
from flask import request
from functools import wraps
from flask import jsonify, abort
from models.news import News

api = Blueprint('api', __name__)

def restful(rule, **options):
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
            return jsonify(res)
        api.add_url_rule(rule, func.__name__, wrapper, **options)
        return wrapper
    return _

@restful('/')
def index():
    # abort(404)
    return 200, 'this is index', 'data'

@restful('/news/<des>')
def get_news(des):
    if isinstance(des, int):
        print '##yes'
        news = News.get(des)
    else:
        print '##no'

        news = News.get_alias(des)
    if news:
        return 200,'', news
    return 404, 'news id not found'

# @restful('/news/<string:aliasname>')
# def get_news(id):
#     news = News.get(id)
#     if news:
#         return 200,'', News.get(id)
#     return 404, 'news id not found'

@restful('/news/hot')
def news_hot():
    data = {}
    start = request.args.get('start', 0)
    rs = News.get_all('create_time', int(start));
    data['count'] = len(rs) if rs else 0
    data['news.list'] = rs
    return 200, 'get hot news ok', data

@restful('/news/popular')
def news_popular():
    data = {}
    start = request.args.get('start', 0)
    rs = News.get_all('comment_count', int(start));
    data['count'] = len(rs) if rs else 0
    data['news.list'] = rs
    return 200, 'get popular news ok', data


# special 404
@restful("/<path:invalid_path>")
def not_found(invalid_path):
    return 404, "There isn't anything at: " + invalid_path



