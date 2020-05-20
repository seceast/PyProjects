"""
-*- coding: utf-8 -*-
@author: yangyd
@file: qiuhe.py
@time: 2019/11/12 0012 16:29
"""
summ = 0
i = 2
while i <= 100:
    if i % 2 == 0:
        summ += i
    else:
        summ -= i
    i += 1

print(summ)
