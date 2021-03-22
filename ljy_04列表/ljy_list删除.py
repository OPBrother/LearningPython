list1 = ['ljy', 'lxm', 559, 596]
list2 = ['张三', '罗翔', '雷军', '马云', '玩尼玛', '王境泽', '马化腾']
list3 = ['老王']

# del 删除列表位置  (关键字 不用括号)
del list2[0]
del list3

# list.pop([index=-1]) 有返回值
list2.pop(-2)
print(list2)

# list.remove(object)  无返回值
list2.remove('雷军')
print(list2)

# list.clear
list1.clear()
print(list1)
