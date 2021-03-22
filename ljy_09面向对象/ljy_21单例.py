'''
单例——只能被一个对象调用的类
例如 播放器只能同时播放一首歌
    软件只能被打开次
'''


class MusicPlayer(object):
    # 记录第一个被创建对象的引用
    instance = None
    # 记录是否执行过初始化动作
    init_flag = False

    # 重写__new__方法 只能让一个对象调用
    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)     # 父类方法返回的是第一个对象的地址
            return cls.instance

        # 把第一次的地址赋值给第二个对象的地址
        return cls.instance                 # 即第二个对象不会调用父类的__new__方法

    # 重写__init__方法 只能让一个对象调用
    def __init__(self):
        if MusicPlayer.init_flag:
            return

        print("播放器初始化")
        MusicPlayer.init_flag = True


# 创建多个对象
player1 = MusicPlayer()
print(player1)

player2 = MusicPlayer()
print(player2)

player3 = MusicPlayer()
print(player3)
