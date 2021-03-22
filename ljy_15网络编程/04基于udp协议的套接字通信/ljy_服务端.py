#!/usr/bin/python
# -*- coding: UTF-8 -*-

import socket               # 导入 socket 模块

#                                   数据报协议-->udp协议
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


server.bind(('127.0.0.1', 8080))   # 0-65535, 1024以前的都被系统保留使用

while True:
    data, client_addr = server.recvfrom(1024)
    server.sendto(data.upper(), client_addr)

server.close()
