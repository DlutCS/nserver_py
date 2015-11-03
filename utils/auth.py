from flask.ext.login import LoginManager
from flask.ext.openid import OpenID
from models.user import User
from appins import app

app.secret_key = 'super secret key'
lm = LoginManager()
lm.init_app(app)
lm.login_view = "main.login"
oid = OpenID(app, '/tmp')

app.config['SESSION_TYPE'] = 'filesystem'

@lm.user_loader
def load_user(id):
    return User.get(id=int(id))

@lm.token_loader
def load_user_from_token(token):
    return User.get_by_token(token)