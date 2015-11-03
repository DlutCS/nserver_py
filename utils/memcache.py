#!/usr/bin/env python
import bmemcached
from functools import wraps
from appins import app
import re
import inspect

'''
Usage:
    @memcache('nserver:category')
    def get_category():
        pass

    @memcache('newsid:<id>')
    def get_news(id):
        pass
    # call
    get_news(id=100)
'''
def memcache(memkey=None, expire=100, clear=False):
    def _(func):
        if not memkey and not clear:
            return func
        if not app.config['MEMCACHE_ON']:
            return func
        host = app.config['MEMCACHE_HOST']
        user = app.config['MEMCACHE_USER']
        passwd = app.config['MEMCACHE_PASS']
        client = bmemcached.Client((host,), user, passwd)

        argspec = inspect.getargspec(func)
        argval = list(argspec.defaults or [])
        argkey = list(argspec.args or [])
        argval = [None]*( len(argkey)-len(argval) ) + argval
        argdict = dict(zip(argkey, argval))

        if clear:
            client.flush_all()
            return func

        @wraps(func)
        def wrapper(*args, **kwargs):
            defarg = argdict.copy()
            defarg.update(kwargs)
            key = memkey
            p = re.compile(r'(\<(\w+?)\>)')
            matches = p.findall(key)
            if matches:
                for (full, name) in matches:
                    if not defarg.has_key(name):
                        raise KeyError('Memcache: cannot find key: %s in kwargs!' % (full))
                    value = str(defarg[name])
                    value = value.replace(r"'", r"\'")
                    value = r"'" + value + r"'"
                    key = key.replace(full, value)
            r = client.get(key)
            if not r:
                print 'Memcache:###not shoot ', key
                r = func(*args, **kwargs)
                client.set(key, r, expire)
            else:
                print 'Memcache:###shooted ', key
            return r
        return wrapper
    return _
