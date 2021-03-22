"""
需求
1.房子有户型、总面积、家具名称列表
新房子没有家具
2.家具有名字，占地面积
    席梦思占地4平米
    衣柜占地2平米
    餐桌占地1.5平米
3.将三件家具添加到房子中
4.打印房子时输出户型、总面积、剩余面积、家具名称列表
"""


class HouseItem:
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return "[%s] 占地 %.2f" % (self.name, self.area)


class House:
    def __init__(self, name, area):
        self.name = name
        self.area = area
        self.free_area = area
        self.item_list = []

    def __str__(self):
        return "户型：%s\n总面积：%.2f[剩余：%.2f]\n家具：%s" \
               % (self.name, self.area,
                  self.free_area, self.item_list)

    def add_item (self, item):
        print("要添加%s" % item)
        # 1.判断家具面积
        if item.area > self.free_area:
            print("%s的面积太大了，无法添加")
            return

        # 2.将家具添加到列表中
        self.item_list.append(item.name)

        # 3.计算剩余面积
        self.free_area -= item.area


# 1.创建家具
bed = HouseItem("席梦思", 4)
cheat = HouseItem("衣柜", 2)
table = HouseItem("餐桌", 1.5)

print(bed)
print(cheat)
print(table)

# 2.创建房子对象
my_home = House("俩室一厅", 60)
my_home.add_item(bed)
my_home.add_item(cheat)
my_home.add_item(table)
print(my_home)


