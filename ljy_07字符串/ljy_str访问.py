str1 = "Hello World!"
str2 = '"Python "Java" print function"'
str3 = "ni\nhao"
# 访问
print(str1[-2])
print(str2[-8:]+''+str1)    # ''里是空的 ' '这样才有空格
val1 = 'i' in str3
print(val1)             # 打印val1是True还是False

for i in str3:
    print(i)                # 遍历

