'''
定义一个工具类
每件工具都要自己的name
需求：想知道这个类创建了多少工具对象
'''


class Tool(object):
    # 使用赋值语句，定义类属性，记录创建工具对象总数
    count = 0
    
    def __init__(self,name):
        self.name = name
        Tool.count += 1         # 类属性 类名.属性名访问


# 1.创建类对象
tool1 = Tool("斧头")
tool2 = Tool("扳手")
tool3 = Tool("水桶")

# 2. 输出工具对象的总数
print(Tool.count)

