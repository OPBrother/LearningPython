list1 = ['ljy', 'lxm', 559, 596]
list2 = ['张三', '罗翔', '雷军', '马云', '玩尼玛', '王境泽', '马化腾']
list3 = ['老王']

# 用for 迭代
for list1_num in list1:
    print(list1_num)

# iteration 迭代
list_iter = iter(list1)
print(next(list_iter))
print(next(list_iter))
print(next(list_iter))
print(next(list_iter))
