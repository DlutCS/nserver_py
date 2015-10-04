from flask import Blueprint, render_template
from views.admin import LoginView, LogoutView

main = Blueprint('main', __name__)


@main.route('/')
def hello_world():
    return "hello, world"

@main.app_errorhandler(404)
def page_not_found(error):
    return render_template('404.html')


# admin
main.add_url_rule('/login', view_func=LoginView.as_view('login'), methods=['GET', 'POST'])
main.add_url_rule('/logout', view_func=LogoutView.as_view('logout'), methods=['GET'])



