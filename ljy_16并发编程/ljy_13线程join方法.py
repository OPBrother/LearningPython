from threading import Thread
import time


def task(name):
    print("%s is running" % name)
    time.sleep(2)
    print("%s is over" % name)


if __name__ == '__main__':
    t = Thread(target=task, args=('egon',))
    t.start()
    # join在start后面
    t.join()
    print('主')