'''
剪刀石头布游戏
'''
import random

a = 0

i = 0
j = 0
k = 0


def game():
    global i, j, k
    player = int(input("请输入剪刀（1）、石头（2）、布（3）"))
    computer = random.randint(1, 3)
    if ((player == 1 and computer == 3)
            or (player == 2 and computer == 1)
            or (player == 3 and computer == 2)):
        print("你太厉害了！")
        i += 1
    elif player == computer:
        print("真是心有灵犀啊！再来一局")
        j += 1
        return game()
    else:
        print("你个菜鸡，连我都比不赢")
        k += 1


while a < 3:
    game()
    a += 1
# print(i,j,k)
print("胜数:%d" % i)
print("平局：%d" % j)
print(" 败数：%d" % k)

