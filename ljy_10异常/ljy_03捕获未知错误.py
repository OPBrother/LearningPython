try:
    num = int(input("请输入一个整数："))
    reslut = 8 / num
    print(reslut)
except ValueError:
    print("请输入正确的整数")
except Exception as r:
    print("未知错误 %s" % r)
