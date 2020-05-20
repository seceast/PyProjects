# -*- coding: utf-8 -*-
# __author__ = yangyd 
# File: database_connection.py
# Create time: 2020/4/30 0030 10:22


import pymysql

connect = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='root',
    db='qq',
    cursorclass=pymysql.cursors.DictCursor
)

if __name__ == '__main__':
    print(connect)
