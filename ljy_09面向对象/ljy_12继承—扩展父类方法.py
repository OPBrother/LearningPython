class Animal:
    def eat(self):
        print("吃")

    def drink(self):
        print("喝")

    def run(self):
        print("跑")

    def sleep(self):
        print("睡")


class Dog(Animal):
    def bark(self):
        print("汪汪汪...")

    def run(self):
        print("pao")


class XiaoTianQuan(Dog):

    def __init__(self):
        # 或 父类名.方法(self）不推荐 修改父类名也要修改这个（了解即可）
        Animal.__init__(self)
        self.age = 200

    def bark(self):
        # 1. 子类特殊的需求
        print("吼吼吼")

        # 2.使用 super().调用原本父类的方法
        super().bark()

        # 3. 增加其他子类的代码
        print("!@#$%$%^%^")


    def fly(self):
        print("我会飞")


wangcai = XiaoTianQuan()
wangcai.eat()
wangcai.run()          # 调用了Dog的方法 没有用Animal
wangcai.bark()
wangcai.fly()
print(wangcai.age)
