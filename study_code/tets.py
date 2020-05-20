"""
-*- coding: utf-8 -*-
@author: yangyd
@file: tets.py
@time: 2019/10/17 0017 09:18
"""

# import wx
#
#
# app = wx.App()
# frame = wx.Frame(None, -1, "Hello, World!")
# frame.Show(True)
# app.MainLoop()

import pymysql

conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='root',
    database='db_lsy_business',
    charset='utf8',
    cursorclass=pymysql.cursors.DictCursor
)

curs = conn.cursor()
name = 'yyd'
sql = "SELECT username FROM tb_user where username = %s"

curs.execute(sql, name)
res = curs.fetchone()
print(res)
