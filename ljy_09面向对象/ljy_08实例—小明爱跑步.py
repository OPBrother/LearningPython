"""
需求
小明体重75.0公斤
小明每次跑步会减肥0.5公斤
小明每次吃东西体重增加1公斤
"""


class Person:
    def __init__(self, name, weight):
        self.name = name
        self.weight = float(weight)

    def run(self):
        print("我的名字叫%s,我爱跑步" % self.name)
        self.weight -= 0.5

    def eat(self):
        print("%s是吃货，吃完这顿再减肥" % self.name)
        self.weight += 1

    # 重写后可以用print（对象）调用改方法
    def __str__(self):
        return "现在%s的体重是%.1f" % (self.name, self.weight)


xiaoming = Person("小明", 75.0)
xiaoming.run()
print(xiaoming)
xiaoming.eat()
print(xiaoming)
