from threading import Thread, active_count, current_thread
import time
import os


def task():
    print('hello world', os.getpid())
    print('线程名', current_thread().name)     # 获取当前线程名
    time.sleep(1)


if __name__ == '__main__':
    t = Thread(target=task)
    t1 = Thread(target=task)
    t.start()
    t1.start()
    print('zhu', active_count())    # 统计当前活跃的线程数
    print('主', os.getpid())
    print('主名', current_thread().name)
