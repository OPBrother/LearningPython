lst = [9, 78, 55, 34, 12, 91, 46, 5, 32]


def func(lst):
    last = len(lst)-1
    while last > 0:
        for i in range(last):
            if lst[i] > lst[last]:
                lst[i], lst[last] = lst[last], lst[i]
        last = last - 1
    return lst


lst = func(lst)
print(lst)
