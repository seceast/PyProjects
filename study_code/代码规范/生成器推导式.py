"""
-*- coding: utf-8 -*-
@author: yangyd
@file: 生成器推导式.py
@time: 2019/10/31 0031 13:33
"""

value = [len(x) for x in open('test.txt')]
# print(value)

# value1 = (len(x) for x in open('test.txt'))
# print(value1)
# print(next(value1))
v_dict = {}

for i, val in enumerate(value):
    v_dict[i] = val
    # print(val)
print(v_dict)
print(v_dict[1])
a = [1, 2, 3, 4, 5, 6, 7]
b = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
a_b = list(zip(a,b))
print(a_b)
c, d = zip(*a_b)
print(c)
print(d)
