# 1.request 发送请求。从服务器获取数据
# 2. BeautiSoup 来解析整个页面的源代码 ->


import requests
from bs4 import BeautifulSoup
import re
import time

n = 1


def get_page(url):
    # 爬取网站的第一件事 发送服务器请求
    resp = requests.get(url)
    resp.raise_for_status()
    resp.encoding = resp.apparent_encoding

    # 解析html
    page = BeautifulSoup(resp.text, "html.parser")
    return page


def save_img(src, adress):
    global n
    # 尝试连接 错误则跳过
    try:
        r = requests.get(src)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        # 创建文件
        '''
        下载视频方法
        response=requests.get('xxx.mp4',
                      stream=True)

        with open('b.mp4','wb') as f:
            for line in response.iter_content():
                f.write(line)
        '''
        f = open(adress+"/tu_%s.jpg" % n, mode="wb")  # wb表示写入内容是非文本文件
        f.write(r.content)  # 向外拿出图片的数据，不是文本信息
        n += 1  # n自增1
        print("恭喜你，下载了一张图片")
        f.close()
        time.sleep(0.2)
    except Exception as r:
        print("未知错误 %s" % r)


def main():
    for i in range(60):
        main_page = get_page(f"http://pic.netbian.com/4kmeinv/index_{2 + i}.html")

        # 从页面中找到某些东西
        # find（） 找一个
        # find () 找所有
        alist = main_page.find("ul", attrs={"class": "clearfix"}).find_all("a", attrs={"target": "_blank"})

        for a in alist:
            # 发送请求到子页面，进入到子页面
            href = "http://pic.netbian.com" + a.get("href")

            child_page = get_page(href)
            # 找到图片的真实路径
            raw_src = child_page.find("div", attrs={"class": "photo-pic"}).find("img").get("src")
            # 发送请求到服务器，把图片保存到本地
            src = 'http://pic.netbian.com'+raw_src
        save_img(src, "E:/image")


main()



