from flask.ext.mysqldb import MySQL
from appins import app
import MySQLdb

mysql = MySQL(app)

def execute(sql, args=None):
    cur = mysql.connection.cursor(cursorclass=MySQLdb.cursors.DictCursor)
    cur.execute(sql, args)
    res = cur.fetchall()
    cur.close()
    return res

def commit():
    last_id = mysql.connection.insert_id()
    mysql.connection.commit()
    return last_id

def rollback():
    mysql.connection.rollback()
