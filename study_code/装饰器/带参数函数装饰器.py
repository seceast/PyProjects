"""
-*- coding: utf-8 -*-
@author: yangyd
@file: 带参数函数装饰器.py
@time: 2019/10/24 0024 10:59
"""


def fun_out(func):
    def fun_in(*args, **kwargs):
        print('装饰器作用：参数*10！')
        args_list = []
        for i in args:
            args_list.append(i*10)
        func(*args_list, **kwargs)

    return fun_in


@fun_out
def add_sum(a, b, c):
    print(f'{a}+{b}+{c}={a + b + c}')


add_sum(1, 2, 5)
