import time
from functools import wraps
'''
1、什么是装饰器
    器：工具  函数或类
    装饰：为其他事物添加额外的东西点缀

    合到一起解释：
        装饰器指的是定义一个函数或类，该函数或类是给其他函数或类添加额外功能的
2、为何要装饰器
    开放封闭原则
        开放：指的是对拓展功能是开放的
        封闭：指的是对修改源代码是封闭的
    装饰器就是在不修改被装饰器对象源代码
3、如何用
'''


# 需求：在不修改index函数的源代码以及调用方式的前提下为其添加统计运行时间
def index(x, y):
    time.sleep(3)
    print('index:%s %s' % (x, y))


# index(111, 222)


# 解决方案一：失败
# 问题：修改了源代码
# def index(x, y):
#     start = time.time()
#     time.sleep(3)
#     print('index:%s %s' % (x, y))
#     stop = time.time()
#     print(stop-start)


# 解决方案二
# 问题：没有修改被装饰对象调用方式，也没有修改源代码并加上新功能
#     但是代码冗余
# start = time.time()
# index(111, 222)
# stop = time.time()
# print(stop-start)


# 解决方案三
# 问题：解决了方案二的代码冗余，但修改了被装饰器对象调用方式
# def wrapper(*args, **kwargs):
#     start = time.time()
#     index(*args, **kwargs)
#     stop = time.time()
#     print(stop-start)
#
#
# wrapper(111,222)


# # 方案三优化二
# # 没有修改被装饰对象的调用方式和源代码，成功
# # 这就是一个闭包函数：wrapper 内部调用形成封闭，outter的参数为一个函数
# # 缺点：返回值---不能返回原函数的返回值
# def home(name):
#     time.sleep(3)
#     print('welcome %s to home page' % name)
#     return 123
#
#
# def outter(func):
#     # func = index
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         func(*args, **kwargs)
#         stop = time.time()
#         print(stop-start)
#     return wrapper
#
#
# # f = outter(index)       # index的内存地址
# # f(111, 222)
# # 偷梁换柱
# index = outter(index)       # index= wrapper的内存地址
# home = outter(home)         # home = wrapper的内存地址
#
# res = home('linjunyu')
# print(res)


# # 方案三优化三:将wrapper做的跟被装饰器一模一样
# def home(name):
#     time.sleep(3)
#     print('welcome %s to home page' % name)
#     return 123
#
#
# def outter(func):
#     # func = index
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         res = func(*args, **kwargs)
#         stop = time.time()
#         print(stop-start)
#         return res
#     return wrapper
#
#
# # f = outter(index)       # index的内存地址
# # f(111, 222)
# # 偷梁换柱
# index = outter(index)       # index= wrapper的内存地址
# home = outter(home)         # home = wrapper的内存地址
#
# res = home('linjunyu')
# print(res)


# # 语法糖：让你开心的语法
# def outter(func):
#     # func = index
#     @ wraps     # 将装饰器的内部属性__name__、__doc__变成原函数的内部属性，伪装的更彻底
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         res = func(*args, **kwargs)
#         stop = time.time()
#         print(stop-start)
#         return res
#     return wrapper
#
# # 在被装饰对象正上方的单独一行写@装饰器名字
# @ outter        # home = outter(home)
# def home(name):
#     time.sleep(3)
#     print('welcome %s to home page' % name)
#     return 123
#
#
#
# index = outter(index)       # index= wrapper的内存地址
# # home = outter(home)         # home = wrapper的内存地址
#
# res = home('linjunyu')
# print(res)

# index(111, 222)
#
# index(111, 222)
#
# index(111, 222)


# # 总结
# # 实现装饰器基本模板
# def outter(func):
#     def wrapper(*args, **kwargs):
#         # 1、调用原函数
#         # 2、为其添加新功能
#         res = func(*args, **kwargs)
#         return res
#     return wrapper

# 计算运行时间的装饰器
# def timmer(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         res = func(*args, **kwargs)
#         stop = time.time()
#         print(stop-start)
#         return res
#     return wrapper
