# coding=utf-8
from selenium import webdriver
import time

# 启动Chrome浏览器
web = webdriver.Chrome()
web.get("https://www.baidu.com")
web.implicitly_wait(10)         # 隐性等待，最长等待10秒  设置一次即可

# 定位搜索框
# id定位：find_element_by_id()
# web.find_element_by_id("kw").send_keys("selenium")
# name定位：find_element_by_name()
# web.find_element_by_name("wd").send_keys("selenium")
# class定位：find_element_by_class_name()
# web.find_element_by_class_name("s_ipt").send_keys("selenium")
# link定位：find_element_by_link_text()
# partial link定位：find_element_by_partial_link_text()
# tag定位：find_element_by_tag_name()
# web.find_element_by_tag_name("input").send_keys("selenium")       失败
# xpath定位：find_element_by_xpath()
# web.find_element_by_xpath('//*[@id="kw"]').send_keys("selenium")
# css定位：find_element_by_css_selector()


# web.find_element_by_css_selector("#kw").send_keys("selenium")


'''# 2.2.1 class含有空格时解决方法：
# 在实际进行元素定位时，经常发现class name是有多个class组合的复合类，中间以空格隔开。如果直接进行定位会出现报错，可以通过以下方式处理：
#
# class属性唯一但是有空格，选择空格两边唯一的那一个
# 若空格隔开的class不唯一可以通过索引进行定位
# self.driver.find_elements_by_class_name('table-dragColumn')[0].click()
# 通过css方法进行定位（空格以‘.’代替）'''
text = web.find_element_by_css_selector('.s-bottom-layer.s-isindex-wrap').text

print(text)

'''
要想调用键盘按键操作需要引入 keys 包：
from selenium.webdriver.common.keys import Keys通过 send_keys()调用按键：
send_keys(Keys.TAB) # TAB
send_keys(Keys.ENTER) # 回车
#ctrl+a 全选输入框内容 
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'a' 
'''

'''
2.7 鼠标事件
鼠标事件一般包括鼠标右键、双击、拖动、移动鼠标到某个元素上等等。
需要引入ActionChains类。
引入方法：
from selenium.webdriver.common.action_chains import ActionChains

ActionChains 常用方法：
perform()  执行所有ActionChains 中存储的行为；
context_click()  右击；
double_click()   双击；
drag_and_drop()  拖动；
move_to_element()  鼠标悬停。
鼠标双击示例：

#定位到要双击的元素
 qqq =driver.find_element_by_xpath("xxx") 
#对定位到的元素执行鼠标双击操作 
 ActionChains(driver).double_click(qqq).perform()
鼠标拖放示例：


#定位元素的原位置 
element = driver.find_element_by_name("source") 
#定位元素要移动到的目标位置 
target = driver.find_element_by_name("target")
#执行元素的移动操作 
ActionChains(driver).drag_and_drop(element, target).perform()
'''



time.sleep(1)

#web.quit()