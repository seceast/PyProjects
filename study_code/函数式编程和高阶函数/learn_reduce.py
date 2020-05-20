"""
-*- coding: utf-8 -*-
@author: yangyd
@file: learn_reduce.py
@time: 2019/9/30 0030 16:09
"""
from functools import reduce

a = [1, 2, 3, 4, 5]
sum = reduce(lambda x, y: x + y, a)
print(sum)


def func(x, y):
    return x * 10 + y


res = reduce(func, a)
print(res)