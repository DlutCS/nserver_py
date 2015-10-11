# -*- coding: utf-8 -*-

from views.api import api, restful, error
from flask import request
from flask import redirect
from utils.consts import *
from models.user import User
import md5
from flask.ext.login import login_user, logout_user, login_required


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
    user = User.create(username, passwd, nickname, gender, birthday, avatar_url)
    if not user:
        return error(10007, u'创建失败')
    return user.dict()

