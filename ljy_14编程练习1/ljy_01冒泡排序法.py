lst = [9, 78, 55, 34, 12, 91, 46, 5, 32]
lst1 = [9, 78, 55, 34, 12, 91, 46, 5, 32]

def funb(lst):

    for i in range(len(lst)-1):
        if lst[i] > lst[i+1]:
            lst[i], lst[i+1] = lst[i+1], lst[i]
    return lst


def bubbleSort(lst1):
    for passnum in range(len(lst1)-1, 0, -1):
        for i in range(passnum):
            if lst1[i] > lst1[i + 1]:
                lst1[i], lst1[i + 1] = lst1[i + 1], lst1[i]
    return lst1


def shortBubbleSort(lst):
    exchange = True
    passnum = len(lst)-1
    while passnum > 0 and exchange:
        exchange = False
        for i in range(passnum):
            if lst[i] > lst[i+1]:
                exchange = True
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
        passnum = passnum-1
    return lst

res = bubbleSort(lst1)
print(res)

res1 = shortBubbleSort(lst)
print(res1)