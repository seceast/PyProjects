"""
-*- coding: utf-8 -*-
@author: yangyd
@file: TCP_server.py
@time: 2019/10/17 0017 15:05
"""

from socket import socket, AF_INET, SOCK_STREAM

# 创建套接字
tcp_server = socket(AF_INET, SOCK_STREAM)
# 绑定服务器端口
tcp_server.bind(("", 8989))
# 监听
tcp_server.listen()
# 接收客户端连接，返回客户端的
client_socket, client_info = tcp_server.accept()

while True:
    # 接收客户端数据
    recv_data = client_socket.recv(1024)
    # 这里使用的时网络调试助手连接，所以使用gb2312解码
    print('客户端信息：%s' % recv_data.decode('utf-8'))
    # 发送消息
    if recv_data.decode('utf-8') == 'bye':
        break
    msg = input(">>")
    client_socket.send(msg.encode('utf-8'))

    # # 关闭连接
client_socket.close()
tcp_server.close()
