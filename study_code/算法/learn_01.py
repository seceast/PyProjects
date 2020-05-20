"""
-*- coding: utf-8 -*-
@author: yangyd
@file: learn_01.py
@time: 2019/10/17 0017 17:44
"""

import time
from builtins import range, print

start_time = time.time()
count = 0
for a in range(1001):
    for b in range(1001):
        c = 1000-a-b
        count += 1
        if a**2+b**2 == c**2:

            print(f'a:{a},b:{b},c:{c}')


end_time = time.time()
print('耗时：{}'.format(end_time-start_time))
print(count)
