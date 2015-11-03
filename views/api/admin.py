# -*- coding: utf-8 -*-

from views.api import api, restful, error
from flask import request
from flask import redirect, url_for
from utils.consts import *
from models.user import User
from models.group import Group
from models.news import News
from models.category import Category
import md5
from flask.ext.login import login_user, logout_user, login_required
from flask.ext.login import current_user
from utils.memcache import memcache

@restful('/admin/login/', methods=['POST'])
def login():
    '''
    username: string 
    passwd: 32bit md5 code
    '''
    try:
        username = request.form['username']
        passwd = request.form['passwd']
    except KeyError:
        return error(400, u'参数错误')
    if len(passwd) == 0 or len(username) == 0:
        return error(10005, u'用户名密码不能为空')
    user = User.validate(username, passwd)
    if not user:
        return error(10006, u'用户名或密码错误')
    login_user(user)
    # login_user(user, remember = remember_me)
    return user.dict()

@restful('/admin/logout/', methods=['POST'])
def logout():
    logout_user()
    return redirect(url_for('main.home'))
    

@restful('/admin/register/', methods=['POST'])
def register():
    try:
        username = request.form['username']
        passwd = request.form['passwd']
        nickname = request.form['nickname']
        gender = request.form['gender']
        birthday = request.form['birthday']
        avatar_url = request.form['avatar_url']
        if len(username)==0 or len(passwd)==0:
            raise(KeyError)
    except KeyError:
        return error(400, u'参数错误')
    if len(gender) == 0:
        gender = 0
    if len(birthday) == 0:
        birthday = '1990-1-1'
    if User.get_by_username(username):
        return error(10008, u'用户已存在')
    passwd = md5.new(passwd).hexdigest()
    user = User.create(username, passwd, nickname, gender, birthday, avatar_url)
    if not user:
        return error(10007, u'创建失败')
    return user

#--------------------------------------------------------------------------------

def admin_require(func):
    action_arr = ['create', 'retrieve', 'update', 'delete']
    def wrapper():
        if not current_user.is_authenticated:
            return error(10111, 'require login')
        args = func.__name__.split('_')
        mod, action = args[0], args[1]
        group_id = User.get(id=current_user.get_id()).group_id
        if not group_id:
            return error(10112, 'user cannot find group id')
        auth_value = Group.get(id=group_id).__getattribute__(mod)
        # print "auth_value=", auth_value
        index = action_arr.index(action)
        index = len(action_arr) - index - 1
        if not (auth_value >> index & 1):
            return error(10113, 'cannot access this action')
        return func()
    return wrapper


#--------------news------------------
@restful('/admin/news/create/', methods=['POST'])
@admin_require
def news_create():
    try:
        title = request.form['title']
        alias_title = request.form['alias_title']
        content = request.form['content']
        cover_url = request.form['cover_url']
        category_id = request.form['category_id']
        auther_id = request.form['auther_id']
    except KeyError:
        return error(400, u'参数错误')
    news = News.create(**locals())
    if not news:
        return error(100021, 'create news failed')
    return news

@restful('/admin/memcache/flush/', methods=['GET','POST'])
@memcache(clear=True)
def memcache_flush():
    return 'ok'
    
@restful('/admin/news/retrieve/', methods=['GET'])
@admin_require
def news_retrieve():
    id = request.args.get('id', 0)
    if id:
        news = News.get(id=id)
        if not news:
            return error(404, 'news not exist')
        return news

    start = request.args.get('start', 0)
    limit = int(request.args.get('limit', PAGE_LIMIT))
    if limit > PAGE_MAX:
        limit = PAGE_MAX
    data = {}
    data['start'] = start
    data['data'] = News.get_all(order='create_time desc', start=int(start), limit=int(limit))
    data['count'] = len(data['data'])
    data['total'] = News.get_total()
    return data


@restful('/admin/news/update/', methods=['POST'])
@admin_require
def news_update():
    valid_column = ['title','author_id','category_id','cover_url','content']
    keys = []
    values = []
    for k, v in request.form.iteritems():
        if k in valid_column and k != 'id':
            keys.append(k)
            values.append(v)

    try:
        id = request.form['id']
        if len(keys) == 0:
            raise KeyError
    except KeyError:
        return error(400, u'参数错误')
    # clause.decode('gb2312').encode('utf-8')
    news = News.update(id, keys, values)
    return news if news else error(10022, 'update news failed')


@restful('/admin/news/delete/', methods=['POST'])
@admin_require
def news_delete():
    print request.form.getlist('id')

    try:
        id = request.form['id'].split(',')
    except KeyError:
        return error(400, u'参数错误')
    if not News.delete(id):
        return error(10020, 'delete failed')
    return 'delete ok'


#--------------category------------------
@restful('/admin/category/create/', methods=['POST'])
@admin_require
def category_create():
    try:
        name = request.form['name']
    except KeyError:
        return error(400, u'参数错误')
    category = Category.create(**locals())
    if not category:
        return error(100021, 'create category failed')
    return category


@restful('/admin/category/retrieve/', methods=['GET'])
@admin_require
def category_retrieve():
    id = request.args.get('id', 0)
    if id:
        category = Category.get(id=id)
        if not category:
            return error(404, 'category not exist')
        return category

    # start = request.args.get('start', 0)
    # limit = int(request.args.get('limit', PAGE_LIMIT))
    # category还要start??, 
    data = {}
    data['start'] = 0
    data['data'] = Category.get_all()
    data['count'] = len(data['data'])

    return data



@restful('/admin/category/update/', methods=['POST'])
@admin_require
def category_update():
    try:
        name = request.form['name']
        id = request.form['id']
    except KeyError:
        return error(400, u'参数错误')
    category = Category.update(**locals())
    if not category:
        return error(10022, 'update category failed')
    return category

@restful('/admin/category/delete/', methods=['POST'])
@admin_require
def category_delete():



    try:
        id = request.form['id'].split(',')
    except KeyError:
        return error(400, u'参数错误')
    if not Category.delete(id):
        return error(10020, 'delete failed')
    return 'delete ok'



#--------------User------------------
@restful('/admin/user/create/', methods=['POST'])
@admin_require
def user_create():
    return redirect(url_for('api.register'), code=307)


@restful('/admin/user/retrieve/', methods=['GET'])
@admin_require
def user_retrieve():
    id = request.args.get('id', 0)
    if id:
        user = User.get(id=id)
        if not user:
            return error(404, 'user not exist')
        return user
    start = request.args.get('start', 0)
    limit = int(request.args.get('limit', PAGE_LIMIT))

    if limit > PAGE_MAX:
        limit = PAGE_MAX

    data = {}
    data['start'] = start
    data['data'] = User.get_all(start=start, limit=limit)
    data['count'] = len(data['data'])
    data['total'] = User.get_total()
    return data

@restful('/admin/user/update/', methods=['POST'])
@admin_require
def user_update():
    try:
        id = request.form['id']
        username = request.form['username']
        passwd = request.form['passwd']
        nickname = request.form['nickname']
        gender = request.form['gender']
        birthday = request.form['birthday']
        avatar_url = request.form['avatar_url']
        group_id = request.form['group_id']
        if len(username)==0 or len(passwd)==0:
            raise(KeyError)
    except KeyError:
        return error(400, u'参数错误')
    user = User.update(**locals())
    if not user:
        return error(10022, 'update user failed')
    return user


@restful('/admin/user/delete/', methods=['POST'])
@admin_require
def user_delete():
    try:
        id = request.form['id'].split(',')
    except KeyError:
        return error(400, u'参数错误')
    if not Category.delete(id):
        return error(10020, 'delete failed')
    return 'delete ok'


