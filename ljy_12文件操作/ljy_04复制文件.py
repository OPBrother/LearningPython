# 1.打开文件（一个源文件，一个新文件）
file1 = open("readme.txt", encoding="UTF-8")
file2 = open("readme[复制].txt", "a")

# 2.读写
while True:
    text = file1.readline()
    file2.write(text)
    if not text:
        break


# 3.关闭文件
file1.close()
file2.close()