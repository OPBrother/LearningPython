"""
一些进程/线程需要等待另一些进程/线程运行完毕之后才能运行，
类似于发射信号一样
"""
from  threading import Thread, Event
import time


event = Event()     # 类似于造了一个红绿灯


def light():
    print("红灯亮着")
    time.sleep(5)
    print("绿灯亮了")
    # 告诉等待红灯的人可以走了
    event.set()
    time.sleep(5)


def car(name):
    print('%s 车正在等红灯' % name)
    event.wait()    # 等待别人给你发信号
    print('%s 车加油门飙车走了' % name)


if __name__ == '__main__':
    t = Thread(target=light)
    t.start()

    for i in range(20):
        t = Thread(target=car, args=('%s' %i,))
        t.start()
