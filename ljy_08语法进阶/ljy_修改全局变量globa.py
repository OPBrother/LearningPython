num = 10


def demo1():
    global num
    num = 19
    print("%d的地址是%d" % (num, id(num)))     # 全局变量


def demo2():

    print("%d的地址是%d" % (num, id(num)))  # 局部变量


demo1()
demo2()
