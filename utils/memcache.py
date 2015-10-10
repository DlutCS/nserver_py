#!/usr/bin/env python
import bmemcached
from functools import wraps
from appins import app

def memcache(key, expire=100):
    def _(func):
        if not app.config['MEMCACHE_ON']:
            return func
        host = app.config['MEMCACHE_HOST']
        user = app.config['MEMCACHE_USER']
        passwd = app.config['MEMCACHE_PASS']
        client = bmemcached.Client((host,), user, passwd)
        @wraps(func)
        def wrapper(*args, **kwargs):
            r = client.get(key)
            if not r:
                r = func(*args, **kwargs)
                client.set(key, r, expire)
            return r
        return wrapper
    return _
