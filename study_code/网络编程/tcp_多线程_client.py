"""
-*- coding: utf-8 -*-
@author: yangyd
@file: tcp_多线程_client.py
@time: 2019/10/17 0017 17:03
"""

from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread

Flag = True  # 设置连接关闭的条件


def readmsg(c_socket):
    while Flag:
        recv_data = c_socket.recv(1024)
        print(f"收到信息：{recv_data.decode('utf-8')}")


def writemsg(c_socket: socket):
    global Flag
    while Flag:
        msg = input('>>:')
        msg = ': '.join((user, msg))
        c_socket.send(msg.encode('utf-8'))
        if msg.endswith('bye'):
            Flag = False
            break


client_socket = socket(AF_INET, SOCK_STREAM)

client_socket.connect(('192.168.1.54', 8989))

# 设置用户名
user = input('输入用户名：')
# 开启一个线程，处理客户端的读取消息
t_read = Thread(target=readmsg, args=(client_socket,))
t_read.start()
# 开启一个线程，处理客户端的发送消息
t_write = Thread(target=writemsg, args=(client_socket,))
t_write.start()

t_read.join()
t_write.join()

client_socket.close()
