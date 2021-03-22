str1 = "Hello World!"
str2 = '"Python "Java" print function'
str3 = "ni\nhao"

# print(str1[-1::-1])     # 反序
# print(str1[::-1])       # 与上面一致
# print(len(str1))        # len
# print(str2.count("n"))  # count
# print(str3.index("h"))  # index
# print(str3.title())     # 首字母大写
# print(str3.upper())     # 全部字母大写
# print(str1.center(20))  # 居中（20个字符）


# strip
# name = '*linjunyu**'
# print(name.strip('*'))     # 去除俩边的*
# print(name.lstrip('*'))     # 去除左边的*
# print(name.rstrip('*'))     # 去除右边的*

# lower、upper
# name = 'LinJunYu'
# print(name.lower())     # 全部小写 lower
# print(name.upper())     # 全部大写 upper

# startswith,endswith
# name = 'alex_SB'
# print(name.startswith('alex'))      # 返回True
# print(name.endswith('SB'))          # 返回True
#
# # format
# res = '我叫{}，性别{}，今年{}岁'.format('林均煜', '男', 23)
# res = '我叫{name}，性别{sex}，今年{age}岁'.format(sex='男', name='林均煜', age=23)
#
# # split
# name = 'root:x:0:0::/root:/bin/bash'
# print(name.split(':'))      # 默认分隔符为空格
# name = 'C:/a/b/c/d.txt'       # 只想拿到顶级目录
# print(name.split('/', 1))     # ['C:', 'a/b/c/d.txt']
# name='a|b|c'
# print(name.rsplit('|', 1))      # 从右开始切分

# # join
# tag = ' '
# print(tag.join(['egon', 'say', 'hello', 'world']))      # 可迭代对象必须都是字符串
#
# # replace
# name = 'alex say :i have one tesla,my name is alex'
# print(name.replace('alex', 'SB', 1))        # 第一个alex换成SB


# 练习
name = " aleX "
# 1)    移除 name 变量对应的值两边的空格,并输出处理结果
# print(name.strip(' '))
# 2)    判断 name 变量对应的值是否以 "al" 开头,并输出结果 
# print(name.startswith('al'))
# 3)    判断 name 变量对应的值是否以 "X" 结尾,并输出结果 
# print(name.endswith('X'))
# 4)    将 name 变量对应的值中的 “l” 替换为 “p”,并输出结果
# print(name.replace("l", "p"))
# 5)    将 name 变量对应的值根据 “l” 分割,并输出结果。
# print(name.split('l'))      # [' a', 'eX ']
# 6)    将 name 变量对应的值变大写,并输出结果 
# print(name.upper())
# 7)    将 name 变量对应的值变小写,并输出结果
# print(name.lower())
# 8)    请输出 name 变量对应的值的第 2 个字符?
# print(name[1])
# 9)    请输出 name 变量对应的值的前 3 个字符?
# print(name[:3])
# 10)    请输出 name 变量对应的值的后 2 个字符? 
# print(name[-2:])
# 11)    请输出 name 变量对应的值中 “e” 所在索引位置? 
# print(name.index('e'))
# 12)    获取子序列,去掉最后一个字符。如: oldboy 则获取 oldbo。
# name =' aleX'
# a = name[:-1]
# print(a)
print(name.strip())
