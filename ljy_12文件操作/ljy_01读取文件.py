# 1.打开文件
file = open("readme.txt", encoding="UTF-8")     # 默认是只读方式 有中文用UFT-8编码
# 2.读写内容
text = file.read()
print(text)
print(len(text))

print("-"*50)
# 读取数据的指针在末尾，再次调用读取不了
text = file.read()
print(text)
print(len(text))

# 3.关闭文件
file.close()
