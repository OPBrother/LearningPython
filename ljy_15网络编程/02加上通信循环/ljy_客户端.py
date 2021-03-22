#!/usr/bin/python
# -*- coding: UTF-8 -*-

import socket

# 1、买手机                     流式协议-->tcp协议
phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2、拨通服务端电话 ip+端口
phone.connect(('127.0.0.1', 8080))

# 3、通信 转成bytes类型
while True:
    msg = input('输入需要发送的消息>>>:').strip()
    if msg == 'quit':
        break
    # bug1 ==== 可以发空，但收不到
    if len(msg) == 0:
        continue
    phone.send(msg.encode('utf-8'))
    data = phone.recv(1024)
    print(data.decode('utf-8'))

# 4、关闭连接（必选的回收资源的操作）
phone.close()