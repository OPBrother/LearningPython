# 记录信息
card_list = []
flag = True


def write():
    file = open("information", "w", encoding="UTF-8")
    file.write(str(card_list))
    file.close()


def read():
    file = open("information", "r", encoding="UTF-8")

    while True:
        text = file.readline()
        for card_info in card_list:
            for i in list(text):
                if i == card_info:
                    print("已经有这个名片了")
                    flag = False
        if not text:
            break

    file.close()


def show_menu():
    """显示菜单"""
    print('*' * 50)
    print('欢迎使用【名片管理系统】v1.0')
    print('1.新建名片\n'
          '2.显示全部\n'
          '3.查询系统\n'
          '\n'
          '0.退出系统')
    print('*' * 50)


def new_Card():
    """
        新增名片
        :return:
    """
    print('-' * 50)
    print('新增名片')
    new_name = input("name:")
    new_sex = input('sex:')
    new_age = int(input('age:'))
    new_dict = {'name': new_name,
                'sex': new_sex,
                'age': new_age}
    read()
    if flag:
        card_list.append(new_dict)
        write()
        print(new_dict)
        print('添加%s的名片成功' % new_name)
    return new_dict


def show_Card():
    """
    显示所有名片
    """
    print('-' * 50)
    '''
    if card_list==[]: # 或者 len(card_list)==0
        print('还没有信息呢')
    else:
        print('显示所以名片')
        for show_name in ['姓名', '性别', '年龄']:
            print(show_name, end='\t\t')
        print('')
        print('=' * 50)
        for card_info in card_list:
            print('%s\t\t%s\t\t%d'%(card_info['name'],
                                      card_info['sex'],
                                      card_info['age']))
    '''
    if len(card_list) == 0:
        print('还没有信息呢')
        return  # if生效执行return后下方代码不生效
    print('显示所以名片')
    for show_name in ['姓名', '性别', '年龄']:
        print(show_name, end='\t\t')
    print('')
    print('=' * 50)
    for card_info in card_list:
        print('%s\t\t%s\t\t%d' % (card_info['name'],
                                  card_info['sex'],
                                  card_info['age']))


'''搜索名片'''


def search_Card():
    print('-' * 50)
    print('搜索名片')
    find_card = input('请输入姓名：')
    for card_info in card_list:
        if find_card == card_info['name']:
            for show_name in ['姓名', '性别', '年龄']:
                print(show_name, end='\t\t')
            print('')
            print('%s\t\t%s\t\t%d' % (card_info['name'],
                                      card_info['sex'],
                                      card_info['age']))
            # 针对找到的信息执行修改和删除操作
            deal_card(card_info)
            break
    else:
        print('没找到%s的名片' % find_card)


"""
    搜索名片后的进一步操作，修改删除名片
    :param find_dict:
    """


def deal_card(find_dict):
    while True:
        ation_str = input('请选择要执行的操作 '
                          '[1]修改 [2]删除 [0]返回上级菜单')
        if ation_str == '1':
            find_dict['name'] = input_card(find_dict['name'], "name【回车不修改】:")
            find_dict['sex'] = input_card(find_dict['sex'], "sex【回车不修改】:")
            find_dict['age'] = input_card(find_dict['age'], "age【回车不修改】:")
            print('修改成功')
            break
        elif ation_str == '2':
            card_list.remove(find_dict)
            print('删除成功')
            break
        elif ation_str == '0':
            break
        else:
            print('输入错误，请重新输入')


"""
    输入函数：如果不输入则不修改变量，如果修改则改变量
    :param card_valure:
    :param tip_message:
    :return:
    """


def input_card(card_valure, tip_message):
    reslut_str = input(tip_message)  # 提示用户输入内容

    if len(reslut_str) > 0:  # 判断是否输入
        return reslut_str  # 输入了就返回修改值
    else:
        return card_valure
