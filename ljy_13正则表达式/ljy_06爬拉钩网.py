from selenium.webdriver import Chrome   # 导入浏览器的包
from selenium.webdriver.common.keys import Keys
import time

key_word = "C++"
n = 1
# 创建浏览器
web = Chrome()

web.implicitly_wait(10)
# 打开浏览器，请求到拉钩
web.get("https://www.lagou.com/")


# 找到关闭按钮，点击
web.find_element_by_xpath('//*[@id="cboxClose"]').click()

# 延时一会
time.sleep(1)

# 找到文本框，输入python，之后回车
web.find_element_by_xpath('//*[@id="search_input"]').send_keys(key_word, Keys.ENTER)

# 延时一会
time.sleep(1)


while True:
    try:
        alist = web.find_elements_by_class_name("position_link")

        for a in alist:
            a.find_element_by_tag_name("h3").click()

            # 窗口转换
            web.switch_to.window(web.window_handles[-1])     # 跳转到最后一个窗口

            job_name = web.find_element_by_class_name('position-head-wrap-name').text

            job_request = web.find_element_by_class_name('job_request').find_element_by_tag_name("h3").text
            # 拿到招聘信息
            job_detail = web.find_element_by_class_name('job_bt').text
            time.sleep(1)
            text = '''
            %d:%s \n %s \n %s
            ''' % (n, job_name, job_request, job_detail)
            # 把招聘信息保存在文本中
            f = open(f"abc/{key_word}.txt", mode="a", encoding='utf-8')
            f.write(text)
            f.close()
            n += 1
            # 关闭窗口
            web.close()
            # 调整窗口到原来页面
            web.switch_to.window(web.window_handles[0])
            time.sleep(2)
        web.find_element_by_class_name('pager_next ').click()
    except:
        pass
