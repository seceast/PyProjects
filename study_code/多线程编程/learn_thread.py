"""
-*- coding: utf-8 -*-
@author: yangyd
@file: learn_thread.py
@time: 2019/10/16 0016 10:48
"""

import threading

# # 获取当前线程对象
# t = threading.current_thread()
# print(t.name)
# # 获取当先活动线程个数
# print(threading.active_count())
#
# # 获取当前主线程
# t1 = threading.main_thread()
# print(t1.name)
import time


def thread_bady():
    """线程体"""
    t = threading.current_thread()
    for i in range(5):
        print(f"第{i}次执行线程{t.name}")
        time.sleep(0.5)
    print(f'线程{t.name}执行完成')


# def main():
#     """主函数"""
#     # 创建线程1，并启动
#     t1 = threading.Thread(target=thread_bady)
#     t1.start()
#     # 创建线程2，并启动
#     t2 = threading.Thread(target=thread_bady)
#     t2.start()
#
#
# main()
if __name__ == '__main__':
    # t1 = threading.Thread(target=thread_bady)
    # t1.start()
    # # 创建线程2，并启动
    # t2 = threading.Thread(target=thread_bady)
    # t2.start()
    print(thread_bady.__doc__)
