"""
-*- coding: utf-8 -*-
@author: yangyd
@file: 辅助函数取代复制表达式.py
@time: 2019/10/30 0030 14:19
"""

from urllib.parse import parse_qs

my_values = parse_qs('red=5&blue=0&green',
                     keep_blank_values=True)

# print(repr(my_values))

print(my_values.get('red'))
print(my_values.get('Green'))

red = my_values.get('red', [''])[0] or 0
Green = my_values.get('Green', [''])[0] or 0
print(red)
print(Green)


# 将以上代码总结为辅助函数
def get_value(values, key, default=0):
    res = values.get(key, [''])
    if res[0]:
        res = int(res[0])
    else:
        res = default
    return res


green = get_value(my_values, 'red')
print(green)
