"""
-*- coding: utf-8 -*-
@author: yangyd
@file: 创建进程.py
@time: 2019/10/16 0016 10:25
"""

from multiprocessing import Process


def run_test():
    print('test')


if __name__ == '__main__':
    print('主进程执行')
    # target接收执行的任务
    p = Process(target=run_test)
    # 调用子进程
    p.start()
