"""
开启进程的两种方式
"""
# 第一种
from multiprocessing import Process
import time


# 定义执行的函数
def task(name):
    print("%s is running" % name)
    time.sleep(3)
    print("%s is over" % name)


if __name__ == '__main__':
    """
    windows操作系统下一定要在main内创建
    因为windows下创建进程类似于模块导入的方式
    会从上往下依次执行代码
    linxu中则是直接将代码拷贝一份
    """
    # Process为类，p为实例化一个对象
    # target= 执行的函数, 参数为元组，容器类型哪怕只有一个元素，建议一定要有逗号隔开
    p = Process(target=task, args=('linjunyu', ))

    # 开启进程
    p.start()   # 告诉操作系统帮你创建一个进程

    print("主")  # 这也是一个进程,异步
    p1 = Process(target=task, args=('lixiangmei', ))
    p1.start()


# # 第二种 类的继承
# # 了解即可
# from multiprocessing import Process
# import time
#
# class MyProcess(Process):
#     def run(self):
#         print("hello,my girl")
#         time.sleep(2)
#         print("I Love You")
#
#
# if __name__ == '__main__':
#     p = MyProcess()
#     p.start()
#     print("主")


