from flask import Flask  
from views.admin import LoginView, LogoutView

app=Flask(__name__)
app.debug = True

@app.route('/')
def hello_world():
    return 'hello, world'

# Example: recommend register like this
app.add_url_rule('/login', view_func=LoginView.as_view('login'), methods=['GET', 'POST'])
app.add_url_rule('/logout', view_func=LogoutView.as_view('logout'), methods=['GET'])


if __name__ == '__main__':  
    app.run()  
