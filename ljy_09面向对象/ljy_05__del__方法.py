class Cat:
    def __init__(self, new_name):
        self.name = new_name

        print("%s来了" % self.name)

    def __del__(self) :      # __del__自动调用
        print("%s 去了" % self.name)


# TOM是一个全局变量
tom = Cat("TOM")
print(tom.name)

# del 关键字可以删除一个对象   没使用的话Cat类里的__del__最后被调用
del tom

print("-"*50)
