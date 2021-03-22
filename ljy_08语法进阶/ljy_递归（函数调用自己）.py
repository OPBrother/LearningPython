def demo(num):

    print(num)

    if num == 1:
        return
    demo(num-1)


# 数字累加 计算1+2+3+...+num
def sum_number(num):

    if num == 1:
        return 1
    temp = sum_number(num-1)
    return num + temp


demo(3)
reslut = sum_number(100)
print(reslut)
