'''
做一个简单的qq密码输入，
用字典保存数据
'''


def login():

    qq_name = int(input('请输入QQ账号：'))
    qq_password = input('请输入QQ密码：')

    dict1 = {qq_name: qq_password}
    print('您的账号密码是：'+ str(dict1))


login()




