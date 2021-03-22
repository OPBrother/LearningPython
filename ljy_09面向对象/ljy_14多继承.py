class A:
    def test(self):
        print("我是父亲")


class B:
    def demo(self):
        print("我是母亲")


class C(A, B):      # 继承多个父类的特性
    pass


c = C()
c.test()
c.demo()

