from ljy_名片系统 import cards_tools


while True:
    cards_tools.show_menu()
    ation_str = input("请选择希望执行的操作")
    print("您的选择的操作是【%s】" % ation_str)

    if ation_str in ["1", "2", "3"]:
        if ation_str == '1':
            cards_tools.new_Card()
        elif ation_str == "2":
            cards_tools.show_Card()
        else:
            cards_tools.search_Card()

    elif ation_str == "0":
        print("欢迎再次使用")
        break
    else:
        print("输入错误！请重新选择！")

