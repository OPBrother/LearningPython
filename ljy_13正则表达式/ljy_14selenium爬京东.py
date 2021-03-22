from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


def get_goods(driver):
    try:
        goods = driver.find_elements_by_class_name('gl-item')
        for good in goods:
            good_href = good.find_element_by_tag_name('a').get_attribute('href')
            # good_name = good.find_element_by_css_selector('.p-name').find_element_by_tag_name('em').text
            good_name = good.find_element_by_css_selector('.p-name em').text
            good_price = good.find_element_by_css_selector('.p-price i').text
            good_commit = good.find_element_by_css_selector('.p-commit a').text

            msg = '''
                    商品名称：%s
                    商品链接：%s
                    商品价格：%s
                    商品评价：%s \n\n
                    ''' % (good_name, good_href, good_price, good_commit)

            with open('jingdong.txt', mode='a', encoding='utf-8') as f:
                f.write(msg)
        button = driver.find_element_by_partial_link_text('下一页')
        button.click()
        time.sleep(1)
        get_goods(driver)
    except Exception:
        pass


def spider(url, keywords):
    driver = webdriver.Chrome()
    driver.get(url=url)
    driver.implicitly_wait(3)

    try:
        input_tag = driver.find_element_by_xpath('//*[@id="key"]')
        input_tag.send_keys(keywords)
        input_tag.send_keys(Keys.ENTER)
        time.sleep(3)
        get_goods(driver)
    finally:
        driver.close()


if __name__ == '__main__':
    spider('https://www.jd.com/', 'iphone12')