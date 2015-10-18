# -*- coding: utf-8 -*-

from flask.views import MethodView
from flask import url_for
from flask import redirect, render_template, request
from models.user import User
from models.forms import LoginForm, RegisterForm
from flask.ext.login import login_user, logout_user, login_required, current_user
from flask import flash


class AdminIndexView(MethodView):

    def get(self):
        if current_user.is_authenticated:
            return render_template('admin/index.html')
        else:
            return '<script>window.location.href="/login?callback=/admin/"+window.location.hash.replace(/^#/,"%23")</script>';

class LoginView(MethodView):

    def get(self):
        loginform = LoginForm()
        callback = request.args.get('callback','/')

        return render_template('login.html', **locals())

    def post(self):
        loginform = LoginForm(request.form)
        callback = request.form.get('callback','/')

        if loginform.validate():
            # add login session 
            print u'Successfully logged in as %s' % loginform.user.username
            login_user(loginform.user, remember=loginform.remember.data)

            return redirect(callback)

        else:
            # return error
            return render_template('login.html', **locals())


class LogoutView(MethodView):

    def get(self):
        logout_user()
        return redirect(url_for('main.home'))


class RegisterView(MethodView):

    def get(self):
        regform = RegisterForm()
        return render_template('register.html', regform=regform)

    def post(self):
        regform = RegisterForm(request.form)
        if regform.validate():
            return redirect(url_for('main.login'))
        return render_template('register.html', regform=regform)
