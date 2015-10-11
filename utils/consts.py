# -*- coding: utf-8 -*-
import time
PAGE_LIMIT = 10

DATE_FORMAT = "%Y-%m-%d"
TIME_FORMAT = "%H:%M:%S"

def now():
    return time.strftime('%s %s' % (DATE_FORMAT, TIME_FORMAT),
                         time.localtime(time.time()))

MAX_SHORT_CONTENT = 100


if __name__ == '__main__':
    print now()