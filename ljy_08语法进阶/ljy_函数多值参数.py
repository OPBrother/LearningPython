# *可以传递多值 一个*代表元组 俩个**代表字典
def demo(num, *args, **kwargs):
    print(num)
    print(args)
    print(kwargs)


def sum_number(*args):
    num = 0

    print(args)
    for n in args:
        num += n

    return num


demo(1, 2, 3, 4, 5, name='小明', age=18)
reslut = sum_number(1, 2, 3)
print(reslut)