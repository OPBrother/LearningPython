
maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 0, 0, 0, 1, 1, 1],
    [1, 0, 1, 1, 1, 1, 0, 0, 1, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 1, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 0, 0, 0, 0, 1, 1, 1],
    [1, 1, 1, 0, 0, 1, 0, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

start = (1, 1)
end = (8, 8)

# 判断当前这个点 上下左右是0是1，如果是0就可以走
# 下边：r+1，c
# 上边：r-1，c
# 左边：r，c-1
# 右边：r，c+1

lst = [start]

while lst:

    # 列表有东西才能继续往下走
    # 当前走到的节点是哪一个节点
    now = lst[-1]
    if now == end:
        print("出来了")
        print(lst)
        break
    row, col = now       # 解构，解包
    maze[row][col] = 2   # 标记这个点已经走过了
    # 下方可以走
    if maze[row+1][col] == 0:
        lst.append((row + 1, col))
        continue
    # 上方可以走
    elif maze[row-1][col] == 0:
        lst.append((row - 1, col))
        continue
    # 左方可以走
    elif maze[row][col-1] == 0:
        lst.append((row, col - 1))
        continue
    # 右方可以走
    elif maze[row][col+1] == 0:
        lst.append((row, col + 1))
        continue
    else:       # 都不让走
        lst.pop()       # 把最后一个退出
else:
    print()
