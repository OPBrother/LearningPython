"""
缺点：长时间占着cpu并且不干活，让cpu不停空转
"""
import socket


server = socket.socket()
server.bind(('127.0.0.1', 8080))
server.listen(5)
server.setblocking(False)

r_list = []
del_list = []

while True:
    try:
        conn, addr = server.accept()
        r_list.append(conn)
    except BlockingIOError as e:
        # print('做其他事')
        # print('列表的长度：', len(r_list))
        for conn in r_list:
            try:
                data = conn.recv(1024)  # 没有消息，报错
                if len(data) == 0:  # 客户端断开链接
                    conn.close()    # 关闭conn
                    # 将无用的conn从r_list删除
                    del_list.append(conn)
                    continue
            except BlockingIOError:
                continue
            except ConnectionResetError:
                conn.close()
                del_list.append(conn)
        # 回收无用的链接
        for conn in del_list:
            r_list.remove(conn)
        del_list.clear()