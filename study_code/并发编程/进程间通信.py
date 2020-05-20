"""
-*- coding: utf-8 -*-
@author: yangyd
@file: 进程间通信.py
@time: 2019/10/17 0017 10:55
"""

from multiprocessing import Queue,Process
import time


def write(q: Queue):
    a = [1, 2, 3, 4, 5]
    for i in a:
        print(f'开始写入{i}')
        q.put(i)
        time.sleep(1)


def reade(q: Queue):
    for i in range(q.qsize()):
        print(f'读取{q.get()}')
        time.sleep(1)


if __name__ == '__main__':
    qu = Queue()
    pw = Process(target=write, args=(qu,))
    pr = Process(target=reade, args=(qu,))
    pw.start()
    pw.join()
    pr.start()
    pr.join()
