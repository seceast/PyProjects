"""
-*- coding: utf-8 -*-
@author: yangyd
@file: tcp_多线程_server.py
@time: 2019/10/17 0017 16:43
"""

from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread

sockets = []


def main():
    server_socket = socket(AF_INET, SOCK_STREAM)

    server_socket.bind(("", 8989))
    server_socket.listen()

    while True:
        client_socket, client_info = server_socket.accept()
        sockets.append(client_socket)
        t = Thread(target=read_msg, args=(client_socket,))
        t.start()

def read_msg(c_socket):
    while True:
        recv_data = c_socket.recv(1024)
        for socket in sockets:
            socket.send(recv_data)


if __name__ == '__main__':
    main()
