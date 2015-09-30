from flask.views import MethodView
from flask import redirect, render_template, request


class LoginView(MethodView):

    def get(self):
        return "Login here"

    def post(self):
        username = request.form["username"]
        password = request.form["password"]
        return 'username={1} password={2}' % (username, password)


class LogoutView(MethodView):

    def get(self):
        return "log out"