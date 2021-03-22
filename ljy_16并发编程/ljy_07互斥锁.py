"""
多个进程同时对一份数据操作的适合，会出现数据错乱的情况
针对上诉问题，解决方法是加锁处理：将并发变成串行，牺牲效率但是保证了数据的安全

扩展:
    1.锁不要轻易的使用，容易造成死锁现象（我们写代码一般不会用到，都是内部封装好了）
    2.锁只在处理数据部分加来保证数据安全
"""
from multiprocessing import Process, Lock
import json
import time
import random


# 查票
def search(i):
    # 文件读取票数操作
    with open("data.json", 'r', encoding='utf-8') as f:
        ticket_dict = json.load(f)

    # 字典取值不要用[]的形式，推荐使用get 因为写的代码打死都不用报错
    # []形式适合赋值操作 如：ticjet_dict[ticket_num] = 2
    print('用户%s查询余票为：%s' % (i, ticket_dict.get('ticket_num')))


def buy(i):
    # 文件读取票数操作
    with open("data.json", 'r', encoding='utf-8') as f:
        ticket_dict = json.load(f)
    # 模拟网络延迟
    time.sleep(random.randint(1, 3))

    # 判断当前是否有票
    if ticket_dict['ticket_num'] > 0:
        ticket_dict['ticket_num'] -= 1
        # 写入数据
        with open("data.json", 'w', encoding='utf-8') as f:
            json.dump(ticket_dict, f)
        print("用户%s买票成功" % i)
    else:
        print("用户%s买票失败" % i)


def run(i, mutex):
    search(i)
    # 给买票环节加锁处理
    # 抢锁
    mutex.acquire()
    buy(i)
    mutex.release()


if __name__ == '__main__':
    # 在主进程中 生成一把锁，让所有的子进程抢，谁先抢到谁先买票
    mutex = Lock()
    for i in range(1, 10):
        p = Process(target=run, args=(i, mutex,))
        p.start()

