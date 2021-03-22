#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 1、一直提供服务
# 2、并发提供服务

import socket               # 导入 socket 模块

"""
s = socket.socket()         # 创建 socket 对象
host = socket.gethostname()  # 获取本地主机名
port = 12345                # 设置端口 # 0-65535, 1024以前的都被系统保留使用
s.bind((host, port))        # 绑定端口

s.listen(5)                 # 等待客户端连接 5指的是半连接池的大小

while True:
    c, addr = s.accept()     # 建立客户端连接。
    print('连接地址：', addr)
    c.send('欢迎访问CodingDict教程！')
    c.close()                # 关闭连接
"""

# 1、买手机                     流式协议-->tcp协议
phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2、绑定手机卡
phone.bind(('127.0.0.1', 8080))   # 0-65535, 1024以前的都被系统保留使用

# 3、开机
phone.listen(5)     # 5指的是半连接池的大小 最多进入五个客户端，类似于五个人在餐馆排队

# 4、等待电话连接请求,拿到电话连接conn
# 加上链接循环(实际上开发不是这样做)
while True:
    conn, client_addr = phone.accept()
    print(conn)
    print("客户端的ip和端口", client_addr)

    # 5、收消息
    while True:
        try:
            data = conn.recv(1024)  # 最大接收的数据量为1024Bytes,收到的是bytes类型
            if len(data) == 0:
                # 在unix系统中，一旦data收到的是空
                # 意味着是一种异常行为：客户度非法断开了连接
                break
            print("客户端发来的消息:", data.decode('utf-8'))
            conn.send(data.upper())
        except Exception:
            # 针对windows系统
            break

    # 6、关闭连接（必须）
    conn.close()

# 7、关机（可选操作）
phone.close()
