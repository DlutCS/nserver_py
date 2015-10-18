from flask.ext.mysqldb import MySQL
from appins import app
import MySQLdb

mysql = MySQL(app)

def execute(sql, args=None, rowscnt=False):
    cur = mysql.connection.cursor(cursorclass=MySQLdb.cursors.DictCursor)
    cur.execute(sql, args)
    rs = cur.fetchall()
    cnt = cur.rowcount
    cur.close()
    return rs if not rowscnt else cnt

def commit():
    last_id = mysql.connection.insert_id()
    mysql.connection.commit()
    return last_id

def rollback():
    mysql.connection.rollback()
