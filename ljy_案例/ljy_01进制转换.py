


def fun():
    num = int(input('请输入一个十进制的整数：'))
    # print(num, '的二进制数为：', bin(num))
    # print(str(num)+'的二进制数为：'+bin(num))
    print('%d的二进制数为：%s', (num, bin(num)))
    print('{0}的二进制数为：{1}'.format(num, bin(num)))        # 格式化字符串的方法
    print(f'{num}的二进制数为：{bin(num)}')                    # 与上行一致

    print(f'{num}的二进制数为：{oct(num)}')
    print(f'{num}的二进制数为：{hex(num)}')



while True:
    try:
        fun()
        break
    except:
        print("输入错误，请重新输入整数")