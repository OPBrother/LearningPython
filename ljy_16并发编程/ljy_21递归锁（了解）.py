"""
递归锁的特点:
    可以被连续的acquire和release
    但只能被第一个抢到这把锁执行上诉操作
    它的内部有一个计数器，每acquire一次计数加一，每release一次计数减一
    只要计数不为0 那么其他人都无法抢到锁
"""
from threading import Thread, Lock, RLock
import time

# mutexA = Lock()
# mutexB = Lock()

# mutexA = RLock()
# mutexB = RLock()  # 这种也不行
# 只有A锁=B锁才可以
mutexA = mutexB = RLock()

class MyThread(Thread):
    def run(self):
        self.func1()
        self.func2()

    def func1(self):
        mutexA.acquire()
        print('%s 抢到A锁' % self.name)
        mutexB.acquire()
        print('%s 抢到B锁' % self.name)
        mutexB.release()
        mutexA.release()

    def func2(self):
        mutexB.acquire()
        print('%s 抢到B锁' % self.name)
        time.sleep(2)
        mutexA.acquire()
        print('%s 抢到A锁' % self.name)
        mutexA.release()
        mutexB.release()


if __name__ == '__main__':
    for i in range(10):
        t = MyThread()
        t.start()