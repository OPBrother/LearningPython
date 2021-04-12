"""
生产者:生产/制作东西的
消费者:消费/处理东西的
该模型除了上述俩个之外还需要一个媒介
    生活中的例子：做包子，包子做好首放在蒸笼（媒介）里，买包子的取蒸笼里面拿
    厨师做菜完后用盘子装着给你消费者端过去

生产者（做包子的）--->消息队列（蒸笼）
"""
from multiprocessing import Process, Queue, JoinableQueue
import time
import random


def producer(name, food, q):
    for i in range(10):
        data = "%s生产了%s%s" % (name, food, i)
        # 模拟延时
        time.sleep(random.randrange(1, 3))
        print(data)
        # 放入队列中
        q.put(data)


def consumer(name, q):
    # 消费者胃口大，光盘行动
    while True:
        food = q.get()
        # if food is None:
        #     break
        time.sleep(random.randrange(1, 3))
        print('%s吃了%s' % (name, food))
        q.task_done()       # 告诉队列你已经取出一个数据完毕了


if __name__ == '__main__':
    # q = Queue()
    q = JoinableQueue()
    p1 = Process(target=producer, args=("大厨egon", "包子", q))
    p2 = Process(target=producer, args=('tank', '馒头', q))
    c1 = Process(target=consumer, args=("春哥", q))
    c2 = Process(target=consumer, args=("牛哥", q))

    p1.start()
    p2.start()
    # 守护进程，当队列取完内部计数器为0时就结束
    c1.daemon = True
    c2.daemon = True
    c1.start()
    c2.start()

    p1.join()
    p2.join()
    # 等待生产者生产完毕之后，往队列中添加特点的结束符号
    # q.put(None)
    q.join()    # 等待队列中所有的数据取完再执行代码
    """
    JoinableQueue 每当我往队列中存数据，内部计数器会＋1
    取出数据时，内部计数器会-1
    q.join() 当计数器为0的时候，才往后运行
    """
