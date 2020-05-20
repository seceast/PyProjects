"""
-*- coding: utf-8 -*-
@author: yangyd
@file: udp_socket.py
@time: 2019/10/16 0016 09:59
"""

from socket import socket, AF_INET, SOCK_DGRAM
# 创建套接字
udp_socket = socket(AF_INET, SOCK_DGRAM)
# 绑定端口,用于接受数据
udp_socket.bind(("", 8989))
# 创建连接地址
addr = ("192.168.1.54", 8080)
# 接受键盘输入信息
data = input("输入信息：")
# 使用sendo发送数据
udp_socket.sendto(data.encode('gb2312'), addr)
# 接收数据
redata = udp_socket.recvfrom(1024)
print(redata[0].decode('gb2312'))

# 关闭连接
udp_socket.close()
