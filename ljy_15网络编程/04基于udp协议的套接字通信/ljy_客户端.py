#!/usr/bin/python
# -*- coding: UTF-8 -*-

import socket               # 导入 socket 模块

#                                   数据报协议-->udp协议
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


while True:
    msg = input('>>>:').strip()
    client.sendto(msg.encode('utf-8'), ('127.0.0.1', 8080))
    data, server_addr = client.recvfrom(1024)
    print(data.decode('utf-8'))

client.close()
