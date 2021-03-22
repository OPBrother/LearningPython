class Women:
    def __init__(self, name, age=18):
        self.name = name
        self.__age = age        # 私有属性

    def __scret(self):
        # 对象的方法内部是可以访问对象的私有属性的
        print("%s的年龄是%d" % (self.name, self.__age))


xiaofang = Women("小芳")


# 打印xiaofang.__age会报错
try:
    xiaofang.__scret()      # 私有对象不能访问会报错
except:
    print("报错了")

print(xiaofang._Women__age)     # 可以用_类名+私有变量和方法名访问，但不推荐
xiaofang._Women__scret()