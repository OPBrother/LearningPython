list1 = ['ljy', 'lxm', 559, 596]
list2 = ['张三', '罗翔', '雷军', '马云', '玩尼玛', '王境泽', '马化腾']
list3 = ['老王']
list4 = [5, 6, 2, 3, 7, 4, 8, 1, 9]
list5 = [5, 3, 5, 4, 5, 6, 5, 7, 6, 4, 5]

# len函数
list1_len = len(list1)
print('列表中包含的元素有%d个' % list1_len)

# list.count（数值）
list5_count = list5.count(5)
print('列表5中5的次数是：%d' % list5_count)

# list.sort 升序
list44 = list4.sort()
print(list44)  # 这样是空的值
print(list4)  # 这个才是对的
list4.sort(reverse=True)  # 降序
print(list4)

# list.reverse 反转
list1.reverse()
print(list1)
