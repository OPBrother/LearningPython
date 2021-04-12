import socket
from threading import Thread
from multiprocessing import Process
"""
服务端
    1、要有固定的IP和PORT
    2、24小时不间断提供服务
    3、能够支持并发
"""

server = socket.socket()
server.bind(('127.0.0.1', 8080))
server.listen(5)


def talk(conn):
    # 通信循环
    while True:
        try:
            data = conn.recv(1024)
            if len(data) == 0:
                break
            print(data.decode('utf-8'))
            conn.send(data.upper())
        except Exception as e:
            print(e)
            break
    conn.close()


# 链接循环
while True:
    conn, addr = server.accept()

    t = Thread(target=talk, args=(conn,))
    t.start()