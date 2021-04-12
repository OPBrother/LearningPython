import time
from concurrent.futures import ThreadPoolExecutor

# 括号内只可以传数字，不传的话默认会开设当前计算机cpu个数的五倍线程
pool = ThreadPoolExecutor(5)    # 池子里固定只有五个线程
"""
池子造出来之后，默认有五个线程
这五个线程不会出现重复创建和销毁的过程
好处：减少开销
使用：
只需将任务放进池子中
"""


def task(n):
    print(n)
    time.sleep(2)
"""
任务的提交方式
    同步：提交任务之后原地等待任务的返回结果，期间不做任何事
    异步：提交任务之后原地不等待任务的返回结果 继续往下执行
"""

# pool.submit(task, 1)    # 朝池子中提交任务  异步提交
# print('主')
t_list = []
for i in range(20):
    res = pool.submit(task, i)
    # print(res.result())     # 这一步代码变成同步提交
    t_list.append(res)

pool.shutdown()     # 关闭线程池 先保证任务全部结束,再返回结果

for t in t_list:
    print('>>>', t.result())
"""
获取函数的返回值用 .result()
但程序从并发变成串行了
"""