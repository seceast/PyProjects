"""
-*- coding: utf-8 -*-
@author: yangyd
@file: learn_nonlocal.py
@time: 2019/10/14 0014 14:33
"""


def outner():
    b = 10

    def inner():
        # 声明外部函数局部变量,不声明可以使用b但是无法修改b
        nonlocal b
        print(f'old_var = {b}')
        b = 20
        print(f'new_bar = {b}')
    inner()


outner()
