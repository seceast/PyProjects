"""
-*- coding: utf-8 -*-
@author: yangyd
@file: lock_thread.py
@time: 2019/10/16 0016 14:22
"""

import threading
import time

# 线程同步，线程锁


# 模拟售票
class TicketDB:

    def __init__(self, count):
        self.ticket_count = count

    def get_ticket_count(self):
        return self.ticket_count

    def sell_ticket(self):
        time.sleep(0.5)  # 添加等待时间，模拟付款时间
        print(threading.current_thread().name)
        print(f'{self.ticket_count}已售出！')
        self.ticket_count -= 1


tb = TicketDB(5)
# 创建线程锁，为了线程同步
lock = threading.Lock()


def thread1_body():
    """线程体函数"""
    global tb, lock
    while True:
        lock.acquire()
        now_ticket = tb.get_ticket_count()
        if now_ticket > 0:
            tb.sell_ticket()
        else:
            lock.release()
            break
        lock.release()
        time.sleep(1)  # 添加等待时间释放cpu，给其他线程启动的机会，否则可能只会使用一个线程


def thread2_body():
    global tb, lock
    while True:
        lock.acquire()
        now_ticket = tb.get_ticket_count()
        if now_ticket > 0:
            tb.sell_ticket()
        else:
            lock.release()
            break
        lock.release()
        time.sleep(1)  # 添加等待时间释放cpu，给其他线程启动的机会，否则可能只会使用一个线程


def main():
    """主函数"""
    # 创建线程1，并启动
    t1 = threading.Thread(target=thread1_body)
    t1.start()
    # 创建线程2，并启动
    t2 = threading.Thread(target=thread2_body)
    t2.start()


main()
