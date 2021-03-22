class A:
    def __init__(self):
        self.num1 = 100
        self.__num2 = 200

    def __test(self):
        print("私有方法%d %d" % (self.num1, self.__num2))

    def test(self):
        print("父类的共有方法 %d" % self.__num2)

        self.__test()


class B(A):
    def demo(self):
        print("父类的方法 %d" % self.num1)

        self.test()            # 用父类的共有方法访问父类的私有方法和属性


b = B()
b.demo()

