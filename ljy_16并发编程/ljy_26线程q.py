"""
同一个进程下多个线程数据是共享的
为什么同一个进程下的线程还使用队列呢
因为队列是
    管道 + 锁
使用用队列还是为了保证数据的安全
"""

import queue
# 现在使用的队列是只能在本地测试使用

# 1 队列q 先进先出
# q = queue.Queue(3)
# q.put(1)
# q.get()
# q.get_nowait()
# q.get(timeout=3)
# q.full()
# q.empty()

# 后进先出q  堆栈：先进后出
# q = queue.LifoQueue(3)
# q.put(1)
# q.put(2)
# q.put(3)
# print(q.get())  # 3

# 优先级q 可以给放入队列中的数据设置进出的优先级
q = queue.PriorityQueue(5)
# put括号内放元组，第一个数字放优先级
# 数字越小，优先级越高
q.put((10, '111'))
q.put((100, '222'))
q.put((0, '333'))
q.put((-5, '444'))
print(q.get())
print(q.get())