a = [1, 2, 3]
b = [1, 2]

b.append(3)
print(id(a))
print(id(b))

print(a == b)   # == 是比较俩个变量的值
print(a is b)   # 身份运算符是比较俩个变量的地址
