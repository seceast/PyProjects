# -*- coding: utf-8 -*-
# @author: yangyd
# @file: nmb_login_data.py
# @time: 2019/9/24 23:09


login_error_data = [
    {'phone': '', 'pwd': '', 'expect': '手机号码或密码不能为空'},
    {'phone': 12233, 'pwd': 2233, 'expect': '手机号码格式不正确'},
    {'phone': 18684720553, 'pwd': '11', 'expect': '密码格式不正确'},
    {'phone': 18684720553, 'pwd': '1111111', 'expect': '错误的账号信息'}
]
