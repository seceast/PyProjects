"""
-*- coding: utf-8 -*-
@author: yangyd
@file: learn_private.py
@time: 2019/10/14 0014 15:50
"""


class PrivateCls:
    __office = '某一大哥'

    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def __work(self):
        print("私有方法")


pc = PrivateCls('yyd', 18)
print(pc.name)
# print(dir(pc))
print(pc._PrivateCls__age)
pc._PrivateCls__work()
print(pc._PrivateCls__office)