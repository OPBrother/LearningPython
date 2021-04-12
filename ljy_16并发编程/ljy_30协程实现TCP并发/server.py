from gevent import monkey
monkey.patch_all()
from gevent import spawn
import socket

"""
服务端
    1、要有固定的IP和PORT
    2、24小时不间断提供服务
    3、能够支持并发
"""

def communication(conn):
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


def server(ip, port):
    server = socket.socket()
    server.bind((ip, port))
    server.listen(5)
    while True:
        conn, addr = server.accept()
        spawn(communication, conn)


if __name__ == '__main__':
    g1 = spawn(server, '127.0.0.1', 8080)
    g1.join()
