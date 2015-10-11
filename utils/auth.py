from flask.ext.login import LoginManager
from flask.ext.openid import OpenID
from models.user import User
import os
from appins import app

lm = LoginManager()
lm.init_app(app)
oid = OpenID(app, '/tmp')

@lm.user_loader
def load_user(id):
    return User.get(int(id))

@lm.token_loader
def load_user_from_token(token):
    return User.get_by_token(token)
