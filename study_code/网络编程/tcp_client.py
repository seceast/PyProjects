"""
-*- coding: utf-8 -*-
@author: yangyd
@file: tcp_client.py
@time: 2019/10/17 0017 15:11
"""

from socket import socket, AF_INET, SOCK_STREAM

client_socket = socket(AF_INET, SOCK_STREAM)

# 调用connect方法连接服务器
client_socket.connect(('192.168.1.54', 8989))

while True:
    msg = input("客户端>>")
    client_socket.send(msg.encode('utf-8'))
    if msg == 'bye':
        break

    recv_data = client_socket.recv(1024)
    print(f"服务端信息{recv_data.decode('utf-8')}")

client_socket.close()
