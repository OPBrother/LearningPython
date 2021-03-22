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
        f = open(adress+"/tu_%s.jpg" % n, mode="wb")  # wb表示写入内容是非文本文件
        f.write(r.content)  # 向外拿出图片的数据，不是文本信息
        n += 1  # n自增1
        print("恭喜你，下载了一张图片")
        f.close()
        time.sleep(0.2)
    except Exception as r:
        print("未知错误 %s" % r)


for i in range(60):
    main_page = get_page(f"https://www.tupianzj.com/meinv/yishu/list_178_{1+i}.html")

    alist = main_page.find("div", attrs={"class": "list_con_box"}).find_all("a")    # , attrs={"target": "_blank"}

    for a in alist:
        # 发送请求到子页面，进入到子页面
        reslut = re.match(r"/meinv/\d", a.get("href"))

        if reslut:
            href = "https://www.tupianzj.com" + a.get("href")

            child_page = get_page(href)
            # 找到图片的真实路径
            src = child_page.find("div", attrs={"id": "bigpic_all"}).find("img").get("src")
            save_img(src, "E:/image")

            text = child_page.find("div", attrs={"class": "pages"}).find("a").text
            num = re.findall("\d+", text)  # list   [15,9,10....]
            for i in range(2, int(num[0]) + 1):  # 把数字加进.html前
                href1 = list(href)
                href1.insert(-5, "_" + str(i))
                href2 = "".join(href1)
                # 找到图片的真实路径
                child_page2 = get_page(href2)
                src = child_page2.find("div", attrs={"id": "bigpic_all"}).find("img").get("src")
                save_img(src, "E:/image")







