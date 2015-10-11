# -*- coding: utf-8 -*-

from flask.views import MethodView
from flask import url_for
from flask import redirect, render_template, request
from models.user import User
from models.form import LoginForm

class LoginView(MethodView):

    def get(self):
        form = LoginForm()
        return render_template('login.html', **locals())

    def post(self):
        #api.login
        #return redirect(url_for("api.login"), code=307)

        form = LoginForm(request.form)
        if form.validate():
            # TODO:  add login session 
            return redirect('/')
        else:
            # return error
            return render_template('login.html', **locals())


class LogoutView(MethodView):

    def get(self):
        return "log out"