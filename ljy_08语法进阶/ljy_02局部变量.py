num=1
def demo1():
    # 函数执行后函数内的变量才创建，函数执行完后变量被回收
    num=10
    print("在demo1函数中的内部变量的地址是%d"%id(num))


demo1()
print(id(num))