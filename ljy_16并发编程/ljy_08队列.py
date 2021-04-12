"""
q.full()
q.empty()
q.get_nowait()
在多进程的情况下不精确
q.put() 放数据
q.get() 取数据
"""
# from multiprocessing import Queue
import queue


# 创建一个队列
q = queue.Queue(5)

q.put(111)
q.put(222)
q.put(333)
print(q.full())     # 判断队列是否满
q.put(444)
q.put(555)
# q.put(666)
print(q.full())


v1 = q.get()
v2 = q.get()
print(q.empty())
v3 = q.get()
v4 = q.get()
v5 = q.get()
print(q.empty())    # 判断队列是否为空
# v6 = q.get()        # 队列中没有数据的话，get方法会停止原地阻塞
# v6 = q.get_nowait()       # 没有数据直接报错
# v6 = q.get(timeout=3)       # 没有数据的话三秒后报错
try:
    v6 = q.get(timeout=3)
    print(v6)
except Exception as e:
    print("队列里没有数据了")
print(v1, v2, v3, v4, v5, )

