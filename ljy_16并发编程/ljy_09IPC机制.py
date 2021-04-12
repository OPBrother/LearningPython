from multiprocessing import Queue, Process
import time
import random
"""
研究思路：
    1、主进程跟子进程借助队列通信
    2、子进程跟子进程借助队列通信
"""


def producer(q):
    q.put('nihao')
    print("hello big baby~")


def consumer(q):
    print(q.get())


if __name__ == '__main__':
    """
    # 主进程与子进程通信
    q = Queue()
    p = Process(target=producer, args=(q,))
    p.start()
    # p.join() get 方法前面不需要join方法，get本身会等待队列数据进来再取
    print(q.get())
    """
    # 子进程与子进程通信
    q = Queue()
    p = Process(target=producer, args=(q,))
    p1 = Process(target=consumer, args=(q,))
    p.start()
    p1.start()