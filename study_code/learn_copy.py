"""
-*- coding: utf-8 -*-
@author: yangyd
@file: learn_copy.py
@time: 2019/10/9 0009 13:59
"""

a = [10, 11]
b = a
b.append(12)
print(a, b)
print(id(a), id(b))
