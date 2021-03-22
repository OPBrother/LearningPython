
lst = [i for i in range(10)]


def sums(lst):
    if len(lst) == 1:
        return lst[0]
    return lst[0] + sums(lst[1:])