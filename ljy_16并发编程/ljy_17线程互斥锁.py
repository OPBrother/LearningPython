from threading import Thread, Lock
import time

money = 100
mutex = Lock()  # 生成锁


def task():
    global money
    mutex.acquire()  # 获取money前加锁，
    tmp = money      # 模拟抢票，不加锁时所有人都拿到100
    time.sleep(0.1)
    money = tmp -1   # 不加锁时所有人都同时减1
    mutex.release()


if __name__ == '__main__':

    t_list = []
    for i in range(100):
        t = Thread(target=task)
        t.start()
        t_list.append(t)
    for t in t_list:
        t.join()
    print(money)    # 不加锁时money为99
