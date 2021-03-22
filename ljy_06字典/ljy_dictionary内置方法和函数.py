dict1 = {'name': '林均煜',
         'sex': '男',
         'age': 22,
         '职业': '学生'}   # 字典最好这样写

dict2 = {'name': 'lxm'
        }

list1 = ['ljy', 'lxm', 559, 596]

# len
print(len(dict1))

# pop 有返回值
print(dict1.pop('sex'))
print(dict1)

# clear 清空
dict2.clear()
print(dict2)

# copy
dict3 = dict1.copy()
print(dict3)

# key
print(dict1.keys())

# fromkeys
dict11 = dict1.fromkeys(list1, 10)
print(dict11)   # {'ljy': 10, 'lxm': 10, 559: 10, 596: 10}

# value
print(dict1.values())

#  .items() 遍历（键，值）
for key, value in dict1.items():
    print(key, value)
