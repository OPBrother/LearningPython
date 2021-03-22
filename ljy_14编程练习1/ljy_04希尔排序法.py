alist = [54, 78, 55, 34, 77, 91, 46, 5, 20]
alist1 = [54, 78, 55, 34, 77, 91, 46, 5, 20]

def shell_sort(lst):
    # 第一步：把列表拆分成三分
    sublistcount = len(alist) // 2
    while sublistcount > 0:
        # 把每分对应的进行比较
        for startpositlon in range(sublistcount):
            gapInsertionSort(alist, startpositlon, sublistcount)
        print("After increments of size", sublistcount,
              "The list is ", alist)
        sublistcount = sublistcount // 2


def gapInsertionSort(alist, start, gap):
    for i in range(start+gap, len(alist), gap):
        currentvalue = alist[i]
        position = i

        while position >= gap and \
            alist[position-gap] > currentvalue:
            alist[position] = alist[position-gap]
            position = position - gap

        alist[position] = currentvalue


shell_sort(alist)

# 另一种
def sort(alist):
    step = len(alist) // 2
    while step > 0:
        for i in range(step, len(alist)):
            while i >= step and alist[i-step] > alist[i]:
                alist[i], alist[i-step] = alist[i-step],alist[i]
                i -= step
        print("After increments of size", step,
              "The list is ", alist)
        step //= 2

sort(alist1)
print(alist1)
