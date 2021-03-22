"""
需求：
士兵 许三多有一把AK47
士兵 可以开火
枪 能发射子弹
枪 装填子弹——增加子弹数量
"""


class Gun:
    def __init__(self, model, bullet_count=0):
        # 1.枪的型号
        self.model = model
        # 2.子弹数量
        self.bullet_count = bullet_count

    def add_bullet(self, count):
        self.bullet_count += count
        print("装弹完成，现在子弹数量：%d", self.bullet_count)

    def shoot(self):
        # 1.判断子弹数量
        if self.bullet_count > 0:
            print("biubiu...")
            self.bullet_count -= 1
        else:
            print("[%s]没子弹了，先装弹" % self.model)


class Soldier:
    def __init__(self, name):
        self.name = name
        self.gun = None         # 新兵没有枪

    def fire(self):

        if self.gun is None:   # 不用 self.gun == None 
            return

        print("冲啊...[%s]" % self.name)
        self.gun.shoot()


# 1.创建枪对象
ak47 = Gun("AK47", 30)

# 2.创建许三多
xusanduo = Soldier("许三多")
xusanduo.gun = ak47             # 一个类的属性可以是另一个类的对象
xusanduo.fire()
