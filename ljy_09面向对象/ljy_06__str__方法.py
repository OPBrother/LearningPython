class Cat:
    def __init__(self, new_name):
        self.name = new_name

        print("%s来了" % self.name)

    def __del__(self) :      # __del__自动调用
        print("%s 去了" % self.name)

    def __str__(self):
        # 该方法必须返回一个字符串
        return "我是小猫[%s]" % self.name


# TOM是一个全局变量
tom = Cat("TOM")
print(tom)
