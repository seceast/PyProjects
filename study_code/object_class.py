"""
-*- coding: utf-8 -*-
@author: yangyd
@file: object_class.py
@time: 2019/10/25 0025 17:06
"""

class C(object):
    a = 1
    def add(self):
        self.a+=1

    @classmethod
    def add2(self):
        self.a+=1

if __name__ == '__main__':
    C.add2()
    C.add2()
    C().add()
    C.add2()
    C().add()
    print(C().a)
    print(C.a)
