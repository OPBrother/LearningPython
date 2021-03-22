'''
异常不会立即中止
会传入调用的主函数
'''


def demo1():
    return int(input("输入整数："))


def demo2():
    return demo1()


# 最终主函数也会出现异常 就可以只在主函数里捕获异常
try:
    print(demo2())
except Exception as r:
    print("未知错误 %s" % r)

