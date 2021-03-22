#      0   1    2  3   4   5   6    7    8
lst = [12, 15, 22, 35, 48, 53, 129, 657, 999]
n = int(input("请输入一个数字:"))

left = 0
right = len(lst) - 1

mid = (left + right) // 2


# 判断
while left <= right:
    if lst[mid] > n:
        # 取小
        right = mid - 1
        mid = (left + right) // 2
    elif lst[mid] < n:
        # 取大
        left = mid + 1
        mid = (left + right) // 2
    else:
        print("找到了,在%s的位置" % mid)
        break
else:       # 当左边大于右边时，数据肯定不存在
    print("对不起，没找到")

