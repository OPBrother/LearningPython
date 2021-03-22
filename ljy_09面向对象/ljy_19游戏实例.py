class Game(object):
    # 历史最高分
    top_score = 0

    def __init__(self, player_name):
        self.player_name = player_name

    @staticmethod               # 静态方法
    def show_help():
        print("游戏帮助提示")

    @classmethod                # 类方法
    def show_top_score(cls):
        print("历史记录 %d" % Game.top_score)

    def start_game(self):       # 实例方法
        print("%s 开始游戏拉..." % self.player_name)


# 1. 查看游戏帮助信息
Game.show_help()
# 2.查看历史最高分
Game.show_top_score()
# 3.创建游戏对象
game = Game("小明")
game.start_game()
