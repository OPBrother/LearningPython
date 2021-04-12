# 1.request 发送请求。从服务器获取数据
# 2. BeautiSoup 来解析整个页面的源代码 ->

import requests
from bs4 import BeautifulSoup
import re
import time

n = 1


def get_page(url):
    global n
    # 爬取网站的第一件事 发送服务器请求
    resp = requests.get(url)
    resp.encoding = "gbk"

    # 解析html
    main_page = BeautifulSoup(resp.text, "html.parser")

    # 从页面中找到某些东西
    # find（） 找一个
    # find () 找所有

    alist = main_page.find("div", attrs={"class": "list"}).find_all("a", attrs={"target": "_blank"})

    for a in alist:
        reslut = re.match("h", a.get("href"))       # 提取不需要的网页
        if not reslut:
            # 发送请求到子页面，进入到子页面
            href = "http://www.netbian.com" + a.get("href")
            resp1 = requests.get(href)
            resp1.encoding = "gbk"
            child_page = BeautifulSoup(resp1.text, "html.parser")
            # 找到图片的真实路径
            src = child_page.find("div", attrs={"class": "pic"}).find("img").get("src")
            # 发送请求到服务器，把图片保存到本地

            # 创建文件
            f = open("E:/image/tu_%s.jpg" % n, mode="wb")    # wb表示写入内容是非文本文件
            f.write(requests.get(src).content)      # 向外拿出图片的数据，不是文本信息
            n += 1 # n自增1
            print("恭喜你，下载了一张图片")
            f.close()
            time.sleep(1)


for i in range(60):
    get_page(f"http://www.netbian.com/weimei/index_{2+i}.htm")




