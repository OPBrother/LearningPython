import re

# 1.从一个字符串中提取到所有数字
list1 = re.findall("\d+","我今年23岁了，我喜欢5个明星")
# print(list1)

# 2.判断一句话中是否有数字
# search的特点：匹配字符串，只匹配第一个结果
res = re.search('\d+', "我今年23岁了，我喜欢5个明星")
#p rint(res.group())

# 3.finditer,所有数据都会匹配，返回是迭代器
it = re.finditer("\d+","我今年23岁了，我喜欢5个明星")
for item in it:
    print(item.group())

# 4.match 从头开始匹配 ^
reslut = re.match('\d+',"23岁了，我喜欢5个明星")
# print(reslut.group())


# split
# reslut1 = re.split("\d+","你好23岁先生。我的间的距离家乐福的进来聊聊看")
# print(reslut1)

# sub 把数字替换成想要的
# reslut2 = re.sub("\d+","_sb_","admin21344岁大撒多")
# print(reslut2)

# obj = re.compile("\d+")
# lst = obj.findall("我今天吃了3个馒头，喝了2碗粥")
# print(lst)


# 爬虫必会的一个重点
# 1.（）括号里的内容是想要的结果
# 2. (?P<name>正则) 把正则匹配到的内容放到name里
# 3. 用group(name)读取
obj = re.compile(r"今天吃了(?P<mian>\d+)碗面，有吃了(?P<xian>\d+)盘小咸菜")
# print(r"你好我叫\n林均煜")         # r不用转义
reslut = obj.finditer("明天我要吃4碗面，喝上8碗汤，今天吃了5碗面，有吃了6盘小咸菜，昨天吃了8碗面，吃了3碗汤")
for item in reslut:
    print(item.group("mian"))
    print(item.group("xian"))