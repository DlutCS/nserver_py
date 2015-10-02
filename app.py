from flask import Flask  
from flask import render_template
from views.admin import LoginView, LogoutView
from models.user import User
from models import db

app=Flask(__name__)
app.config.from_envvar('CONFIG_FILE')
db.init_app(app)


@app.route('/')
def hello_world():
    return 'hello, world %r' % User.query.all()[0].username

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html')

# admin
app.add_url_rule('/login', view_func=LoginView.as_view('login'), methods=['GET', 'POST'])
app.add_url_rule('/logout', view_func=LogoutView.as_view('logout'), methods=['GET'])


if __name__ == '__main__':  
    app.run()  
