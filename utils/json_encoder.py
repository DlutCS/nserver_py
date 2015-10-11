# -*- coding: utf-8 -*-

import datetime
from models import Model
from flask import json
from .consts import *

class ModelEncoder(json.JSONEncoder):
    def default(self, o):
        if issubclass(o.__class__, Model):
            data = {}
            fields = o.__json__() if hasattr(o, '__json__') else dir(o)
            for field in [f for f in fields if not f.startswith('_') and f not in ['metadata']]:
                value = o.__getattribute__(field)
                ty = type(value)
                try:
                    json.dumps(value)
                    if ty is datetime.datetime:
                        value = value.strftime("%s %s" % (DATE_FORMAT, TIME_FORMAT))
                    elif ty is datetime.date:
                        value = value.strftime("%s" % (DATE_FORMAT))
                    elif ty is datetime.time:
                        value = value.strftime("%s" % (TIME_FORMAT))
                    data[field] = value
                except TypeError:
                    pass
                    # data[field] = None
            return data
        return json.JSONEncoder.default(self, o)


