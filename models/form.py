# -*- coding: utf-8 -*-

from wtforms import Form, BooleanField, StringField, PasswordField, validators

class LoginForm(Form):
    username = StringField(u'用户名', [validators.Length(min=4, max=16)])
    password = PasswordField(u'密码', [validators.Length(min=6, max=16)])
    remember = BooleanField(u'记住我', [validators.Optional()])