from wtforms import Form, BooleanField, TextField, PasswordField, validators
from .user import User


class LoginForm(Form):
    username = TextField('username', [validators.Length(min=4, max=25)])
    passwd = PasswordField('New Password', [
                validators.Required(),
                validators.EqualTo('confirm', message='Passwords must match')
            ])