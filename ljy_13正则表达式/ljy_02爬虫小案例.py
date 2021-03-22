# 1. 从服务器获取到网页源代码（url.request）
from urllib.request import Request, urlopen
import re


def get_page(url):
    # 1.请求信息
    r = Request(url, headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36 Edg/88.0.705.68"
    })
    resp = urlopen(r)      # 发送请求
    return resp.read().decode("utf-8")

# 2. 从网页源代码中提取到你想要的数据（re）
# 先准备好re
def parse_page(s):
    obj = re.compile(r'<div class="item">.*?'
                     r'<em class="">(?P<rate>.*?)</em>.*?'
                     r'<span class="title">(?P<name>.*?)</span>.*?'
                     r'<span class="rating_num" property="v:average">(?P<rating_num>.*?)</span>.*?'
                     r'<span>(?P<person_num>.*?)</span>', re.S)       # re.S可以让正则中的.匹配换行符
    res = obj.finditer(s)   # 匹配
    lst = []
    for item in res:        # 循环结果
        dic = item .groupdict()     # 每次循环都是一个电影信息
        lst.append(dic)
    return lst



if __name__ == '__main__':
    f = open("movies.txt", mode="w", encoding="utf-8")
    for i in range(10):
        s = get_page(f"https://movie.douban.com/top250?start={i*25}&filter=")
        reslut = parse_page(s)
        for d in reslut:
            f.write(str(d))
            f.write("\n")
    f.close()
