from selenium import webdriver
import time

web = webdriver.Chrome()
web.get("https://movie.douban.com/top250")
web.implicitly_wait(3)

while 1:
    alist = web.find_elements_by_class_name("item")
    f = open('mo.text', mode='a', encoding='utf-8')

    for a in alist:

        rate = a.find_element_by_class_name('pic').text
        name = a.find_element_by_class_name('title').text
        rate_num = a.find_element_by_class_name('rating_num').text
        try:
            geyan = a.find_element_by_class_name('quote').text
        except Exception as r:
            print("未知错误 %s" % r)

        f.write(rate)
        f.write(',')
        f.write(name)
        f.write(',')
        f.write(rate_num)
        f.write(',')
        f.write(geyan)
        f.write('\n')
    web.find_element_by_class_name("next").click()
    time.sleep(1)
    f.close()


