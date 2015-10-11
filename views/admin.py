# -*- coding: utf-8 -*-

from flask.views import MethodView
from flask import url_for
from flask import redirect, render_template, request
from models.user import User


class LoginView(MethodView):

    def get(self):
        return "Login here"

    def post(self):
        return redirect(url_for("api.login"), code=307)


class LogoutView(MethodView):

    def get(self):
        return "log out"