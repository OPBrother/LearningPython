lst = [9, 78, 55, 34, 12, 91, 46, 5, 32]


def insert_sort(lst):
    for index in range(1, len(lst)):    # 从1到n-1遍历
        while index > 0 and lst[index-1] > lst[index]:
            lst[index], lst[index-1] = lst[index-1], lst[index]
            index -= 1

    return lst


res = insert_sort(lst)
print(res)