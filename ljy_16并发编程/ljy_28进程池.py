import time
import os
from concurrent.futures import ProcessPoolExecutor

# 括号内只可以传数字，不传的话默认会开设当前计算机cpu个数的进程
pool = ProcessPoolExecutor(5)


def task(n):
    print(n, os.getpid())
    time.sleep(2)
"""
任务的提交方式
    同步：提交任务之后原地等待任务的返回结果，期间不做任何事
    异步：提交任务之后原地不等待任务的返回结果 继续往下执行
        异步提交任务的返回结果,应该通过回调机制来获取
        回调机制
            就相当于给每个异步任务绑定了一个定时炸弹
            一旦任务有结果立即触发炸弹
"""


def call_back(n):
    print('call_back >>>', n.result())


if __name__ == '__main__':

    # t_list = []
    for i in range(20):
        pool.submit(task, i).add_done_callback(call_back)
        # print(res.result())     # 这一步代码变成同步提交
        # t_list.append(res)

    # pool.shutdown()     # 关闭线程池 先保证任务全部结束,再返回结果
    # for t in t_list:
    #     print('>>>', t.result())
