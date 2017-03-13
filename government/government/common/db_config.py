# coding=utf-8
__author__ = 'YANGJINHUA963'
import MySQLdb


def db_conn():
    conn = MySQLdb.connect(
        host='10.25.27.90',
        port=3306,
        user='yangjinhua963',
        passwd='12345678',
        db='AutomationDashboard',
        )
    cur = conn.cursor()
    cur.close()
    conn.commit()
    conn.close()
    print "+++++++++++++++++++++++++++++test+++++++++++++++++++++++++++++++++++++++"
    return cur
