"""
-*- coding: utf-8 -*-
@author: yangyd
@file: 进程池.py
@time: 2019/10/17 0017 09:57
"""

import multiprocessing
import time


def func(msg):
    print('start:', msg)
    time.sleep(3)
    print('end:', msg)


if __name__ == '__main__':
    # 创建进程池3
    pool = multiprocessing.Pool(3)
    for i in range(1, 6):
        msgs = f'任务{i}'
        pool.apply_async(func, (msgs,))

    pool.close()  # 如果不在接收新的请求，调用close
    pool.join()
