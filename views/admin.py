# -*- coding: utf-8 -*-

from flask.views import MethodView
from flask import url_for
from flask import redirect, render_template, request
from models.user import User
from models.forms import LoginForm
from flask.ext.login import login_user, logout_user, login_required
from flask import flash


class LoginView(MethodView):

    def get(self):
        form = LoginForm()
        return render_template('login.html', **locals())

    def post(self):
        #api.login
        #return redirect(url_for("api.login"), code=307)

        # if request.headers['X-Requested-With'] == 'XMLHttpRequest':
            # return '{"msg":"this is ajax"}'

        form = LoginForm(request.form)
        if form.validate():
            # add login session 
            print u'Successfully logged in as %s' % form.user.username
            login_user(form.user, remember=form.remember.data)
            return redirect('/')
        else:
            # return error
            return render_template('login.html', **locals())


class LogoutView(MethodView):

    def get(self):
        logout_user()
        return redirect(url_for('main.home'))