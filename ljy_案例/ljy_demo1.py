from turtle import *  # 调画布
import random  # 使用随机数模块
import time  # 使用time模块计算时间

n = 100.0  # 基础的位移值

speed("fastest")  # 设置速度
screensize(bg='seashell')  # 背景颜色 海贝壳色 偏粉色
left(90)  # 画笔本身是向右的，通过向左旋转，变为竖直向上方向
forward(3 * n)  # 树干300个单位长
color("orange", "yellow")  # 设置指针颜色，外框橙色，内部黄色
begin_fill()  # 封闭图形开始起点
left(126)  # 画树干，转126度画星星

for i in range(5):  # for循环5次，五角星一个角一次
    forward(n / 5)  # 线长，向前二十个单位，即五角星的边长为二十
    right(144)  # 向右旋转144度
    forward(n / 5)  # 再次按照新的方向前进二十个单位
    left(72)  # 向左旋转72度
end_fill()  # 封闭图形结束点
right(126)  # 画笔转正，令指针回到向上的方向

color("dark green")  # 树干的颜色改为黑绿色

backward(n * 4.8)  # 画笔退回到最下边，后退480，令指针达到最下方，完成圣诞树主干的绘制


def tree(d, s):  # 定义了一个d s
    if d <= 0: return  # 判断d如果d小于等于0回去，不运行下边的程序
    forward(s)  # 前进
    tree(d - 1, s * .8)  # tree函数自己调用自己
    right(120)
    tree(d - 3, s * .5)
    right(120)
    tree(d - 3, s * .5)
    right(120)
    backward(s)  # 定义tree回到最初的位置


tree(15, n)  # 使用tree
backward(n / 2)
