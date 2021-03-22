list1 = ['ljy', 'lxm', 559, 596]
list2 = ['张三', '罗翔', '雷军', '马云']
list3 = ['老王']
# 直接赋值不能改不存在的值
print(list1)
list1[0] = 'lxm'
print(list1)

# list.append 追加值
list2.append('马化腾')
print(list2)

# list.insert（index,obiect)
list1.insert(3, 520)
print(list1)

# list.extend 扩展
list3.extend(['玩尼玛', '王境泽'])
list3.extend(list2)
print(list3)



