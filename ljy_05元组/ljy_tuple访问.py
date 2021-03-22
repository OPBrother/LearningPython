tuple1 = ('ljy', 'lxm', 559, 596)
tuple2 = ('张三', '罗翔', '雷军', '马云', '马云')

# 访问
print(tuple1[1])
print(tuple2[:3])

# 创建新元组，元组里不能修改
tuple3 = tuple2 + tuple1
print(tuple3)

print(tuple3.index('罗翔'))
print(tuple3.count('马云'))

# 删除
del tuple1
print(tuple3)
