# -*- coding: utf-8 -*-

from appins import app
from flask import Flask, Blueprint
from views.api import api
from views import main
from utils.json_encoder import ModelEncoder
from flask.ext.login import current_user
from models.category import Category
import re
app.json_encoder = ModelEncoder

import sys   
reload(sys)
sys.setdefaultencoding('utf8') 

@app.context_processor
def static_processor():
    def static_for(path):
        rmEnd = re.compile("/$")
        rmBegin = re.compile("^/")
        return rmEnd.sub('',app.config['STATIC_ROOT'])+ '/' + rmBegin.sub('',path)

    def static_admin_for(path):
        rmEnd = re.compile("/$")
        rmBegin = re.compile("^/")
        return rmEnd.sub('',app.config['STATIC_ADMIN_ROOT'])+ '/' + rmBegin.sub('',path)
    return dict(static_admin_for=static_admin_for, static_for=static_for)

@app.context_processor
def inject_categories():
    return dict(categories=Category.get_all())

app.register_blueprint(main, url_prefix='')
app.register_blueprint(api, url_prefix='/api')

from utils.auth import *


if __name__ == '__main__':  
    app.run()  
