from math import pi

# squares = []
#
# for x in range(10):
#     squares.append(x**2)
# print(squares)

# 列表推导式
squares = list(map(lambda x: x**2, range(10)))
print(squares)

# 列表推导式
lst = [x**2 for x in [-4, -2, 0, 2, 4]]
print(lst)

# combs = []
# for x in [1, 2, 3]:
#     for y in [3, 1, 4]:
#         if x != y:
#             combs.append((x, y))
# 等价下面
combs = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
print(combs)

lst1 = [str(round(pi, i)) for i in range(1, 6)]
print(lst1)