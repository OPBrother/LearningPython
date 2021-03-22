class Dog(object):
    # 先用修饰器来标识
    @staticmethod
    def run():          # 静态方法不需要传入（self）

        # 静态方法 不需要访问 实例属性/类属性
        print("小狗要跑...")


Dog.run()