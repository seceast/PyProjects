# -*- coding: utf-8 -*-
# __author__ = yangyd 
# File: learn_01.py
# Create time: 2019/12/16 0016 09:45

from pywinauto import application

app = application.Application("uia").start(r"D:\Programs\Dict\YoudaoDict.exe")

# 进程号链接
# app = application.Application("uia").connect(process=13140)
# print(app)
# 窗口句柄链接
# app = application.Application("uia").connect(handle=327890)
# print(app)

dlg = app['网易有道词典']
dlg.minimize()

dlg.close()
# dlg.print_control_identifiers()
