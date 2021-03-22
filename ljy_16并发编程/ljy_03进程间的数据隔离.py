from multiprocessing import Process

money = 100


def task():
    # 局部修改全局
    global money
    money = 666
    print("子", money)


if __name__ == '__main__':
    p = Process(target=task)
    p.start()
    p.join()
    print("主", money)
