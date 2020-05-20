# -*- coding: utf-8 -*-
# @author: yangyd
# @file: login_data.py
# @time: 2019/8/30 10:53 


login_error_data = [
    {'phone': '', 'pwd': '', 'expect': '账号不能为空'},
    {'phone': 12233, 'pwd': '', 'expect': '密码不能为空'},
    {'phone': 18684720553, 'pwd': '1111', 'expect': '请输入6-24位密码'}
]


login_success_data = [
    {'phone': 19915986907, 'pwd': 'yyd19915986907', 'expect': '+ 加入课程'}
]
