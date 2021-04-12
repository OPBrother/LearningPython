"""
开设进程
    1、申请内存空间    耗资源
    2、”拷贝代码“     耗资源

开线程
    一个进程内可以开设多个线程，在用一个进程内开始多个线程
    无需再次申请内存空间

总结：开设进程的开销要远远的小于进程的开销

例如：我们要开发一款文本编辑器
    获取用户输入的功能
    实时展示到屏幕的功能
    自动保存到硬盘功能
针对上面三个功能，开设进程还是线程合适？
    开三个线程处理
"""
from threading import Thread
import time

"""
def task(name):
    print('%s is running' % name)
    time.sleep(2)
    print('%s is over' % name)


# 开启线程不需要在main下面执行代码，直接书写就可以
# 但是习惯上将启动命令写在main下面
if __name__ == '__main__':
    t = Thread(target=task, args=('egon', ))
    t.start()
    print('主')"""



class MyThread(Thread):
    def __init__(self, name):
        self.name = name
        # 重写了别人的方法 又不知道别人的方法里有啥 你就调用父类的方法
        super().__init__()

    def task(name):
        print('%s is running' % name)
        time.sleep(2)
        print('%s is over' % name)


if __name__ == '__main__':
    t = MyThread('egon')
    t.start()
    print('主')