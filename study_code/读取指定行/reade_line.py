# -*- coding: utf-8 -*-
# @author: yangyd
# @file: reade_line.py
# @time: 2019/9/18 10:50 


import linecache


class ReadLine:
    x = 3

    @property
    def y(self):
        return '666'
    line = linecache.getline(r'test.txt', 3)
    # print(type(line))


rl = ReadLine()
rl.x = 5
print(rl.y)
print(rl.x)
