"""
当监管对象只有一个的时候，其实IO多路复用连阻塞IO都比不上
但是IO多路复用可以一次性监管多个对象

监管机制是操作系统本身就有的，如果想要用该监管机制（select）
想用就需要导入对应的select模块
"""
import socket
import select


server = socket.socket()
server.bind(('127.0.0.1', 8081))
server.listen(5)
server.setblocking(False)
read_list = [server]

while True:
    r_list, w_list, x_list = select.select(read_list, [], [])
    for i in r_list:
        ''' 针对不同对象做不同的处理'''
        if i is server:
            conn, addr = i.accept()
            # 也应该添加到带监管的队列中
            read_list.append(conn)
        else:
            try:
                res = i.recv(1024)
                if len(res) == 0:
                    i.close()
                    # 将无效的监管对象移除
                    read_list.remove(i)
                    continue
                print(res)
                i.send(b'heiheihei')
            except ConnectionResetError:
                i.close()
                read_list.remove(i)
                continue