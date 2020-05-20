"""
-*- coding: utf-8 -*-
@author: yangyd
@file: 创建子进程并传递参数.py
@time: 2019/10/16 0016 10:40
"""

from multiprocessing import Process
from time import sleep


def run_test(name, **kwargs):
    print(f'子进程运行name为{name}')
    print(f'字典的值为：{kwargs}')


if __name__ == '__main__':
    print('zhu')
    p = Process(target=run_test, args=("test",), kwargs={"age": 12})
    p.start()
