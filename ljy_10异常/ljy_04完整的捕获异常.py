try:
    num = int(input("请输入一个整数："))
    reslut = 8 / num
    print(reslut)
except ValueError:
    print("请输入正确的整数")
except Exception as r:
    print("未知错误 %s" % r)
else:
    print("正确输入才会被执行")
finally:
    print("finally函数无论是否出现错误都会被执行的代码")

print("-"*50)
