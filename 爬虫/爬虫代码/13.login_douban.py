#coding=utf-8

from selenium import webdriver
import time


class DouBan():

    def __init__(self):
        self.driver = webdriver.Chrome()


    def get_cook(self):
        '''获取cookies'''
        cookies = {i["name"]:i["value"] for i in self.driver.get_cookies()}
        return cookies

    def run(self):
        self.driver.get("https://www.douban.com/")
        time.sleep(3)
        self.driver.switch_to.frame(self.driver.find_element_by_tag_name('iframe'))
        self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/ul[1]/li[2]').click()
        time.sleep(3)
        self.driver.find_element_by_id("username").send_keys("15193252279")
        self.driver.find_element_by_id("password").send_keys("930819@lg")
        self.driver.find_element_by_class_name("account-form-field-submit").click()

        time.sleep(10)

        #获取cook
        print(self.get_cook())
        time.sleep(5)

        self.driver.close()


#
# def main():
#
#     options = webdriver.ChromeOptions()
#     options.add_argument(
#         'user-agent=" Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36"')
#     driver = webdriver.Chrome(chrome_options=options)
#     driver.get("https://www.douban.com/")
#
#     # 切换到子框架
#     driver.switch_to.frame(driver.find_element_by_tag_name('iframe'))
#     # 先点击账号密码登录的按钮
#     driver.find_element_by_xpath('/html/body/div[1]/div[1]/ul[1]/li[2]').click()
#     time.sleep(3)
#     driver.find_element_by_id("username").send_keys("15193252279")
#     driver.find_element_by_id("password").send_keys("930819@lg")
#
#     time.sleep(3)
#
#     driver.find_element_by_class_name('account-form-field-submit ').click()
#
#     time.sleep(12)
#     driver.close()



if __name__ == '__main__':
   db = DouBan()
   db.run()