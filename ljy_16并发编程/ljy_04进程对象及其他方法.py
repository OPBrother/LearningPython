"""
一台计算机上运行着很多进程，，那么如何区分和管理呢？
计算机会给每个运行的进程分配一个PID号（进程号）
如何查看
    windows电脑 进入终端输入tasklist即可查看
    具体进程号 $ tasklist |findstr PID号
    mac 进入终端输入ps aux查看
"""
from multiprocessing import Process, current_process
import time
import os


def task():
    print("%s is running" % current_process().pid)  # 查看当前进程的进程号
    print("子进程的主进程号：%s" % os.getppid())
    time.sleep(3)


if __name__ == '__main__':
    p = Process(target=task)
    p.start()
    p.terminate()   # 杀死当前进程  同时进行
    time.sleep(0.1)
    print(p.is_alive())     # 判断当前进程是否存活
    """
    一般情况下会将布尔值的变量名和返回结果
    的布尔值的方法名都起成is_开头
    """
    print("主", os.getpid())     # 查看当前进程的进程号 这种方法更好
    print("主主", os.getppid())       # 获取父进程pycharm的pid号
