# -*- coding: utf-8 -*-

from wtforms import Form, BooleanField, TextField, PasswordField, validators,StringField
from .user import User
import md5


class LoginForm(Form):

    username = StringField(u'用户名', [validators.Length(min=4, max=16)])
    password = PasswordField(u'密码', [validators.Length(min=6, max=16)])
    remember = BooleanField(u'记住我', [validators.Optional()])

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)
        self.user = None

    def validate(self):
        rv = Form.validate(self)
        if not rv:
            return False
        _passwd = md5.new(self.password.data).hexdigest()
        user = User.validate(self.username.data, _passwd)
        if not user:
            self.username.errors.append('Unknown username or password')
            return False
        self.user = user
        return True