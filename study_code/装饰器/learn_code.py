# -*- coding: utf-8 -*-
# @author: yangyd
# @file: learn_code.py
# @time: 2019/9/6 10:42 

"""
装饰器函数:
1、函数嵌套函数
2、外层函数返回内部嵌套函数的函数名
3、外层函数接收一个参数（被装饰的函数名）
4、被装饰的函数在装饰函数内部函数中调用
"""


# 闭包函数
def permission(func):
    """
    装饰器函数（权限鉴定函数）
    :param func: 需要装饰的函数名
    :return: 返回内部嵌套的函数
    """
    def login():
        user = str(input("请输入用户名："))
        pwd = str(input("请输入密码："))
        if user == 'yyd' and pwd == 'yyd':
            func()
        else:
            print("用户名或者密码错误！")
    return login


@permission
def update_info():
    print('修改用户信息的函数')


update_info()

#
# def permission(func):
#     def login(a, b):
#         print("装饰器功能函数")
#         func(a, b)
#     return login
#
#
# @permission
# def add(a, b):
#     print(f'{a}+{b}={a+b}')
#
#
# add(2, 5)
