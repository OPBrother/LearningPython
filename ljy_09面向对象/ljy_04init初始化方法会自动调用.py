class Cat:
    def __init__(self, name):
        print("我正在被调用...")
        self.name = name


tom = Cat("TOM")
print(tom.name)
