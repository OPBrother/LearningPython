# 定义类名 首字母大写（大驼峰法）
class Person:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex                  # 没使用的变量尽量不要定义

    def eat(self):
        print("我是%s" % self.name)
        print("我饿了，我要吃吃吃")

    def sleep(self):
        print("我是%s" % self.name)
        print("我困了，我要睡觉了")


P1 = Person("林均煜", 18, "男")
P2 = Person("李湘梅", 16, "女")
P1.sleep()
P2.eat()
print(P1)
