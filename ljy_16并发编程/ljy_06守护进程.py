"""
守护进程：父进程活着子进程活着，父进程死亡子进程死亡，该子进程就是守护进程
"""
from multiprocessing import Process
import time


def task(name):
    print("%s总管正在活着" % name)
    time.sleep(3)
    print("%s总管正在死亡" % name)


if __name__ == '__main__':
    p = Process(target=task, args=("egon", ))
    p.daemon = True     # 将p设置成守护进程，这句一定要放在start前面，否则报错
    p.start()
    time.sleep(2)
    print("皇帝寿终正寝")