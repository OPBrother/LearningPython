"""
进程:资源单位
线程:执行单位
协程:单线程下实现并发
    程序员在代码层面检测我们所有的IO操作
    一旦遇到IO 我们在代码级别完成切换
    这样给cpu感觉就是程序一直在运行 没有IO
    从而提升运行效率

多道技术:
    切换+保存状态
    cpu的俩种切换
    1、程序遇到IO
    2、程序长时间占用

TCP服务端
    accept、recv都是IO操作

代码如何做到
    切换 + 保存状态
    切换

    保存状态
       保存上一次我执行的状态，下次来接着上一次的操作继续往后执行
       yield
"""
import time
from gevent import monkey      # 猴子补丁
monkey.patch_all()
from gevent import spawn
"""
gevent模块本身无法检测常见的IO操作
在使用时需要导入额外的一句
"""


# def func1():
#     while True:
#         1000000 + 1
#         yield
#
#
# def func2():
#     g = func1()
#     for i in range(100000):
#         i + 1
#         next(g)

def heng():
    print('哼')
    time.sleep(2)
    print("哼")


def ha():
    print('哈')
    time.sleep(3)
    print('哈')


start_time = time.time()
g1 = spawn(heng)
g2 = spawn(ha)
g1.join()
g2.join()
# heng()
# ha()
end_time = time.time()
print(end_time - start_time)
