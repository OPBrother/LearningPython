"""
信号量在不同的阶段可能对应不同的技术点
在并发编程中信号量指的是锁!!!

如果我们将互斥锁比喻成一个浴室的话
那么信号量就相对于多个浴室
"""
from threading import  Thread, Semaphore
import time
import random

# 括号内写数字，写几就表示开设几个浴室
sm = Semaphore(5)


def task(name):
    sm.acquire()
    print('%s 正在洗澡' % name)
    time.sleep(random.randint(1,5))
    sm.release()


if __name__ == '__main__':
    for i in range(20):
        t = Thread(target=task, args=('特种兵%s号' % i,))
        t.start()


