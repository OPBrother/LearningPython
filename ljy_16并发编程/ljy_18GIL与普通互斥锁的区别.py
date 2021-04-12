from threading import Thread, Lock
import time

mutex = Lock()
money = 100


def task():
    global money
    # with mutex:
    #     tmp = money
    #     time.sleep(0.1)
    #     money = tmp -1
    mutex.acquire()
    tmp = money
    time.sleep(0.1)
    money = tmp - 1
    mutex.release()


if __name__ == '__main__':
    t_list = []
    for i in range(100):
        t = Thread(target=task)
        t.start()
        t_list.append(t)
    for t in t_list:
        t.join()
    print(money)
