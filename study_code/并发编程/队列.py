"""
-*- coding: utf-8 -*-
@author: yangyd
@file: 队列.py
@time: 2019/10/17 0017 10:44
"""

from multiprocessing import Queue


# 创建队列,可以设置队列大小，不指定默认无限
q = Queue(3)
# put方法插入队列，可选两个参数
q.put('msg1')
q.put('msg2')
q.put('msg3')
# q.put('msg4', block=True, timeout=1)

# get方法获取并删除元素
print(q.get(block=True,timeout=1))