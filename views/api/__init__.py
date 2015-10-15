# -*- coding: utf-8 -*-

from flask import Blueprint, url_for, redirect
from flask import request
from flask import Response
from flask import make_response
from functools import wraps
from flask import jsonify, abort
from flask import json
from utils.consts import *


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
            if issubclass(r.__class__, Response) or issubclass(Response, r.__class__): # a normal Response
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

from news import *
from admin import *

# special 404
@restful("/<path:invalid_path>/")
def not_found(invalid_path):
    return error(404, "There isn't anything at: " + invalid_path)



