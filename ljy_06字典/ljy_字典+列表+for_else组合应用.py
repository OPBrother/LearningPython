card_list = [
    {"name":'张三',
     'qq':12345678,
     'phone':7777775555},
    {"name":'李四',
     'qq':87654321,
     'phone':7138775555}]

find_name = '张三1'
for card_info in card_list:
    print(card_info)
    if find_name == card_info['name']:
        break
else:
    print('没找到%s' % find_name)