'''
类方法 ：

'''


class Tool(object):
    # 使用赋值语句，定义类属性，记录创建工具对象总数
    count = 0

    @classmethod     #首先标识这个
    def show_tool_count(cls):
        # 访问类属性用 cls.属性名
        print("工具对象的数量%d" % cls.count)

    def __init__(self, name):
        self.name = name
        Tool.count += 1  # 类属性 类名.属性名访问


# 1.创建类对象
tool1 = Tool("斧头")
tool2 = Tool("扳手")
tool3 = Tool("水桶")

# 2. 访问类方法用——类名.类方法
Tool.show_tool_count()

