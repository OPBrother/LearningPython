def test(num):
    print("在函数内部%d对于的内存地址是%d" % (num, id(num)))
    num = 20
    reslut = "hello"

    print("函数要返回数据的内存地址是%d" % id(reslut))
    # 返回的是数据的引用，而不是数据本身
    return reslut


# 1.定义一个数字变量
a = 10

# 数据的内存地址本质是一个数字
print("a变量保存的数据内存地址是%d" % id(a))

# 调用函数时 形参本质上传递的是实参保存数据的引用(地址)，而不是实参保存的数据
var1 = test(a)
print("%s的内存地址是%d" % (var1, id(var1)))
print(a)