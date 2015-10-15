from flask import Blueprint, render_template
from views.admin import LoginView, LogoutView, RegisterView, AdminIndexView
from views.home import HomeView, HomeCategoryView, HomeNewsView

main = Blueprint('main', __name__)


@main.app_errorhandler(404)
def page_not_found(error):
    return render_template('404.html')

main.add_url_rule('/', view_func=HomeView.as_view('home'), methods=['GET'])

# admin
main.add_url_rule('/admin/', view_func=AdminIndexView.as_view('admin'), methods=['GET'])
main.add_url_rule('/register/', view_func=RegisterView.as_view('register'), methods=['GET', 'POST'])
main.add_url_rule('/login/', view_func=LoginView.as_view('login'), methods=['GET', 'POST'])
main.add_url_rule('/logout/', view_func=LogoutView.as_view('logout'), methods=['GET'])

main.add_url_rule('/category/<int:cid>/', view_func=HomeCategoryView.as_view('category'), methods=['GET'])
main.add_url_rule('/news/<nid>/', view_func=HomeNewsView.as_view('news'), methods=['GET'])



