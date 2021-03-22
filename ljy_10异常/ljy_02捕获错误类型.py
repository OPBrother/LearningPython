try:
    num = int(input("请输入一个整数："))
    reslut = 8 / num
    print(reslut)
except ValueError:
    print("请输入正确的整数")
except ZeroDivisionError:
    print("0不能做除数")