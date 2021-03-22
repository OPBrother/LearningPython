dict1 = {'name': '林均煜',
         'sex': '男'}
dict2 = {'name':'lxm'}

tuple1 = ('ljy', 'lxm', 559, 596)
tuple2 = ('张三', '罗翔','雷军','马云','马云')
dict3 = {tuple1: tuple2}
print(dict3)                # y元组的key 可以是数字、字符串、元组，但不可是列表

#   取值
print(dict1["name"])

#   增加/修改
dict1['age'] = 22
print(dict1)
dict1['age'] = 23
print(dict1)

# 删除
del dict1['age']
print(dict1)

