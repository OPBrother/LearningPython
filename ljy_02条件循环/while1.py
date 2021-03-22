'''
九九乘法表
'''


'''
def chengfa():
    
    # 这个是九九乘法表
    
    a = 1
    while a <= 9:
        b = 1
        while b <= a:
            c = a*b
            print("%d * %d = %d\t" % (a, b, c), end=" ")
            b += 1
        print("")
        a += 1


chengfa()
'''
dic={
    'egon1':{'password':'123','count':0},
    'egon2':{'password':'123','count':0},
    'egon3':{'password':'123','count':0},

}

while True:
    name = input("请输入用户名:")

    if name not in dic:
        print("用户名不存在")
        continue
    if dic[name]['count'] >2:
        print('系统锁定')
        continue
    password = input('请输入密码')

    if password == dic[name]['password']:
        print('登录成功')
        break
    else:
        print('登录失败')
        dic[name]['count'] += 1
