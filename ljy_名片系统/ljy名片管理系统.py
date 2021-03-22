'''
*********************************
欢迎使用【名片管理系统】v1.0

1.新建名片
2.显示全部
3.查询系统

0.退出系统
'''


def print_welcome():
    print('*'*50)
    print('欢迎使用【名片管理系统】v1.0')
    print('1.新建名片\n'
          '2.显示全部\n'
          '3.查询系统\n'
          '\n'
          '0.退出系统')
    print('*'*50)


def new_Card ():
    new_name=input("name:")
    new_sex=input('sex:')
    new_age=int(input('age:'))
    new_dict={'name':new_name,
              'sex':new_sex,
              'age':new_age}
    print('您输入的是',end='')
    print(new_dict)
    return  new_dict


def show_Card ():
    if card==[]:
        print('还没有信息呢')
    else:
        for card_info in card:
            print(card_info)


def find_Card ():
    find_card=input('请输入姓名：')
    for card_info in card:
        if find_card == card_info['name']:
            print(card_info)
            break
    else:
        print('没找到%s' % find_card)


card = []
flag = True
while flag:
    print_welcome()
    input_num = int(input('请选择操作功能:'))
    if input_num == 1:
        new_card = new_Card()
        card.append(new_card)
    elif input_num == 2:
        show_Card()
    elif input_num == 3:
        find_Card()
    elif input_num == 0:
        flag = False
    else:
        print('输入错误，请重新输入!')