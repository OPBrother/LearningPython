# 1.打开
# w(只写) 没有搜到文件会新建文件
# a(追加)append的意思 文件指针放在末尾写入，如果该文件不存在，创建新文件进行写入
file = open("readme.txt", "a", encoding="UTF-8")

# 2.写入
file.write("hello，我叫林均煜")

# 3.关闭
file.close()
