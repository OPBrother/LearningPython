"""
同一进程下的多线程无法利用多核优势，是不是就没有用了
多线程是否有用要看具体情况
单核：四个任务（IO密集型 | 计算密集型）
多核：四个任务（IO密集型 | 计算密集型）

# 计算密集型     每个任务都需要10s
单核（不用考虑了）
    多进程：额外的消耗资源
    多线程：介绍开销
多核：
    多进程：总耗时 10s+
    多线程：总耗时 40s+
# IO密集型
多核
    多进程：相对浪费资源
    多线程：更加节省资源
"""

from multiprocessing import Process
from threading import Thread
import os
import time

"""
多进程和多线程都有各自的优势
并且我们后面在写项目的时候通常可以
    多进程下再开设多线程
这样的话既可以利用多核也可以介绍资源消耗
"""

"""
# 计算密集型
# 开多进程好


def work():
    res = 0
    for i in range(1, 10000000):
        res *= i


if __name__ == '__main__':
    l = []
    print(os.cpu_count())
    start_time = time.time()
    for i in range(12):
        p = Process(target=work)
        p.start()
        l.append(p)
    for p in l:
        p.join()
    print(time.time()-start_time)   # 2.469942569732666
    # for i in range(12):
    #     t = Thread(target=work)
    #     t.start()
    #     l.append(t)
    # for t in l:
    #     t.join()
    # print(time.time()-start_time)   # 6.539082288742065
"""


# IO密集型
# 多线程好
def work():
    time.sleep(2)


if __name__ == '__main__':
    l = []
    print(os.cpu_count())
    start_time = time.time()
    # for i in range(40):
    #     p = Process(target=work)
    #     p.start()
    #     l.append(p)
    # for p in l:
    #     p.join()
    # print(time.time()-start_time)   # 5.625787258148193
    for i in range(40):
        t = Thread(target=work)
        t.start()
        l.append(t)
    for t in l:
        t.join()
    print(time.time()-start_time)   # 2.0112204551696777
