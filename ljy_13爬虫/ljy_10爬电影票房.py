from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select #导入Select包
import re
import time

'''
使用Selcet需要导入该模块的包

导入模块方法：from selenium.webdriver.support.select import Select

一般使用3种方法来定位：

通过索引来定位: select_by_index()

通过文本值来定位：select_by_visible_text()

通过value值来定位： select_by_value()
'''


web = webdriver.Chrome()
web.implicitly_wait(5)
web.get("https://www.endata.com.cn/BoxOffice/BO/Year/index.html")


n = 0
while n < 14:
    # ele 定位元素
    ele = web.find_element_by_id('OptionDate')
    ele.click()
    # 悬停鼠标
    ActionChains(web).move_to_element(ele).perform()
    time.sleep(1)
    # 选择对话框里的并点击
    Select(ele).select_by_value(f"{2021-n}")
    n += 1
    time.sleep(1)

    # 拿每行的数据作为列表
    tbody = web.find_element_by_css_selector('.bo-table.img-table').find_element_by_tag_name('tbody')
    lst = tbody.find_elements_by_tag_name('tr')

    f = open('piaofang.csv', mode='a', encoding='utf-8')

    for a in lst:
        # 对数据分割        [换行符 空格]
        text = re.split('[\n  ]', a.text)

        # text = a.text.strip()   # 默认去掉左右俩端的空白（空格，制表符，换行符）
        for c in text:
            c = c.replace(',', '')
            f.write(c)
            f.write(',')
        f.write('\n')
    f.close()
    

