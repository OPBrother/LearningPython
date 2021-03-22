class Cat:
    def eat(self):
        print("小猫爱吃鱼")

    def drink(self):
        print("小猫要喝水")


# 创建猫对象
tom = Cat()
# 可以使用赋值语句 对象名.赋值    但不推荐使用，并没有对类的创建属性
tom.name = "TOM"
tom.eat()
tom.drink()
print(tom)
lazy_cat = Cat()
lazy_cat.name = "大懒猫"
lazy_cat.eat()
lazy_cat.drink()
print(lazy_cat)
