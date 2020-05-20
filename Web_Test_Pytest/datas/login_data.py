# -*- coding: utf-8 -*-
# @author: yangyd
# @file: login_data.py
# @time: 2019/8/30 10:53 


login_error_data = [
    {'phone': '', 'pwd': '', 'expect': '请输入手机号'},
    {'phone': 12233, 'pwd': 2233, 'expect': '请输入正确的手机号'},
    {'phone': 18684720553, 'pwd': '', 'expect': '请输入密码'}
]

login_unauthorized_data = [
    {'phone': 13888888888, 'pwd': 2233, 'expect': '此账号没有经过授权，请联系管理员!'},
    {'phone': 18684720553, 'pwd': 2233, 'expect': '账号或密码错误！'}
]

login_success_data = [
    {'phone': 18684720553, 'pwd': 'python', 'expect': '退出'}
]
