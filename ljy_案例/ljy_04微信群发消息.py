import csv
from wxpy import *
import time

def read_info():
    f = open('./')
    reader = csv.DictReader(f)
    return [info for info in reader]        # list 列表解析式


def make_msg(raw_info):
    t = '{n}-同学请于{t}时间参加{s}课程，课程地址是{a}。收到请回复，谢谢！'
    return [t.format(n=info['姓名'],
                     t=info['上课时间'],
                     s=info['课程'],
                     a=info['上课地址']) for info in raw_info]
    # ‘姓名','上课时间' 等为字典key
    # -> list ['xxx...', 'xxx...',...]


def send(msg_list):
    bot = Bot()
    for msg in msg_list:
        fren_name = msg.split('-')[0]
        f = bot.friends().search(fren_name)
        if len(f) == 1:
            f[0].send(msg)
        else:
            print(fren_name)
            print('Please check this name')
            time.sleep(3)
# bot->bot.find_fren() -> bot.send()
# f = bot.friends().search('name')
# f.send('msg')


raw_info = read_info()
msg = make_msg(raw_info)
send(msg)
