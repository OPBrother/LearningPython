class MusicPlayer(object):
    def __new__(cls, *args, **kwargs):
        # 1.创建对象时，new方法会最先被自动调用
        print("创建对象，分配空间")             # 因为重写了__new__方法，而没有返回引用对象

        # 2.为对象分配空间
        instance = super().__new__(cls)     # 调用了父类的__new__方法

        # 返回对象引用
        return instance

    def __init__(self):
        print("播放器初始化")


player = MusicPlayer()
print(player)
