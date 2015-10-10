# -*- coding: utf-8 -*-

from views.api import api, restful, error
from flask import request
from utils.consts import *
from models.user import User
import md5


@restful('/admin/login/', methods=['POST'])
def login():
    try:
        username = request.form['username']
        passwd = request.form['passwd']
    except KeyError:
        return error(400, 'request error')
    if len(passwd) == 0 or len(username) == 0:
        return error(10005, u'用户名密码不能为空')
    print username, passwd
    user = User.validate(username, passwd)
    if not user:
        return error(10006, u'用户名或密码错误')
    return user
    
@restful('/admin/register/', methods=['POST'])
def register():
    try:
        username = request.form['username']
        passwd = request.form['passwd']
        nickname = request.form['nickname']
        gender = request.form['gender']
        birthday = request.form['birthday']
        avatar_url = request.form['avatar_url']
    except KeyError:
        return error(400, '请求错误')
    if User.get_by_username(username):
        return error(10008, u'用户已存在')
    user = User.create(username, passwd, nickname, gender, birthday, avatar_url)
    if not user:
        return error(10007, u'创建失败')
    return user

