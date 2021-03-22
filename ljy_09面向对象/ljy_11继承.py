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

    def bark(self):
        print("吼吼吼")    # 父类方法不能满足子类，就重名重写

    def fly(self):
        print("我会飞")


wangcai = XiaoTianQuan()
wangcai.eat()
wangcai.run()          # 调用了Dog的方法 没有用Animal
wangcai.bark()
wangcai.fly()
