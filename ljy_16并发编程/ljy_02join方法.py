"""
join方法: 主进程等待子进程后完成后才执行
"""
from multiprocessing import Process
import time


def task(name, n):
    print("%s is running" % name)
    time.sleep(n)
    print("%s is over" % name)


if __name__ == '__main__':
    """ 
    p1 = Process(target=task, args=('linjunyu', 1,))
    p2 = Process(target=task, args=('lixiangmei', 2,))
    p3 = Process(target=task, args=('nihh', 3), )
    start_time = time.time()
    p1.start()
    p2.start()
    p3.start()
    # 主进程等待进程p运行结束后再继续执行
    p1.join()
    p2.join()
    p3.join()
    # 总时间为3秒多,三个进程同时进行，取决于最久的
    print("主", time.time() - start_time)
    """

    start_time = time.time()
    # for相当于把三个子进程串行
    for i in range(1, 4):
        p = Process(target=task, args=('子进程%s' %i, i))
        p.start()
        p.join()
    print("主", time.time() - start_time)