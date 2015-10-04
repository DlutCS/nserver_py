# -*- coding: utf-8 -*-

from flask import Flask, Blueprint
from models import mysql
from views.api import api
from views import main
from utils.json_encoder import ModelEncoder

app = Flask(__name__)
app.config.from_pyfile('default.cfg', silent=True)
app.json_encoder = ModelEncoder
mysql.init_app(app)

app.register_blueprint(main, url_prefix='')
app.register_blueprint(api, url_prefix='/api')


if __name__ == '__main__':  
    app.run()  
