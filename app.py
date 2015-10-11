# -*- coding: utf-8 -*-

from appins import app
from flask import Flask, Blueprint
from views.api import api
from views import main
from utils.json_encoder import ModelEncoder
from flask.ext.login import current_user
from models.category import Category

app.json_encoder = ModelEncoder

@app.context_processor
def static_processor():
    def static_for(path):
        return app.config['STATIC_ROOT'] + path
    return dict(static_for=static_for)

@app.context_processor
def inject_categories():
    return dict(categories=Category.get_all())

app.register_blueprint(main, url_prefix='')
app.register_blueprint(api, url_prefix='/api')


if __name__ == '__main__':  
    app.run()  
