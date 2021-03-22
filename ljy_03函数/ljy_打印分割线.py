# def print_line (char='*'):
#     print(char*50)
#
# print_line('-')


def print_line(char='*', times=50):
    """
    打印分割线
    :param char: 字符
    :param times: 次数
    """
    print(char * times)


def print_lines(char, times):
    row = 0
    while row < 5:
        print_line(char, times)
        row += 1


print_lines('-', 20)
