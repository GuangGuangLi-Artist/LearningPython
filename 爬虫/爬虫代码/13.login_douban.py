#coding=utf-8

from selenium import webdriver
import time


# class DouBan():
#
#     def __init__(self):
#         self.driver = webdriver.Chrome()
#
#
#     def get_cook(self):
#         '''获取cookies'''
#         cookies = {i["name"]:i["value"] for i in self.driver.get_cookies()}
#         return cookies
#
#     def run(self):
#         self.driver.get("https://www.douban.com/")
#         time.sleep(3)
#         iframe = self.driver.find_elements_by_xpath("//*[@id='anony-reg-new']/div/div[1]/iframe")
#         self.driver.switch_to_frame(iframe)
#         self.driver.find_element_by_class_name("account-tab-account on").click()
#         time.sleep(3)
#         self.driver.find_element_by_id("username").send_keys("15193252279")
#         self.driver.find_element_by_id("password").send_keys("930819l@g")
#         self.driver.find_element_by_class_name("btn btn-account").click()
#
#         time.sleep(10)
#
#         #获取cook
#         print(self.get_cook())
#
#         self.driver.close()



def main():

    options = webdriver.ChromeOptions()
    options.add_argument(
        'user-agent=" Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36"')
    driver = webdriver.Chrome(chrome_options=options)
    driver.get("https://passport.csdn.net/login?code=public")
    driver.find_elements_by_xpath('//*[@id="app"]/div/div/div[1]/div[2]/div[5]/ul/li[2]/a')[0].click()
    time.sleep(3)
    driver.find_element_by_id("all").send_keys("15193252279")
    driver.find_element_by_id("password-number").send_keys("930819@lg")
    driver.find_elements_by_xpath('//*[@id="app"]/div/div/div[1]/div[2]/div[5]/div/div[6]/div/button')[0].click()
    time.sleep(10)
    driver.close()


if __name__ == '__main__':
   main()