"""
-*- coding: utf-8 -*-
@author: yangyd
@file: 线程间通信.py
@time: 2019/10/16 0016 14:51
"""

import threading
import time

# 创建条件变量
event = threading.Event()


class Stack:

    def __init__(self):
        self.pointer = 0  # 堆栈指针初始为0
        self.data_list = [-1, -1, -1, -1, -1]

    def push(self, data):
        """压栈方法"""
        while self.pointer == len(self.data_list):
            event.wait()
        event.set()
        self.data_list[self.pointer] = data
        self.pointer += 1

    def pop(self):
        """出栈方法"""

        while self.pointer == 0:
            event.wait()
        event.set()
        self.pointer -= 1
        return self.data_list[self.pointer]


stack = Stack()


def create_thread_body():
    global stack

    for i in range(10):
        stack.push(i)
        print(f'生产{i}')
        time.sleep(1)


def consume_thread_body():
    global stack

    for i in range(10):
        res = stack.pop()
        print(f'消费{res}')
        time.sleep(1)


def main():
    """主函数"""
    # 创建线程1，并启动
    t1 = threading.Thread(target=create_thread_body)
    t1.start()
    # 创建线程2，并启动
    t2 = threading.Thread(target=consume_thread_body)
    t2.start()


main()
