file = open("readme.txt", "r", encoding="UTF-8")

while True:
    # readline 逐行读取，内存压力没怎么大
    text = file.readline()

    if len(text) == 0:      # 判断是否读取内容
        break
    print(text)


file.close()