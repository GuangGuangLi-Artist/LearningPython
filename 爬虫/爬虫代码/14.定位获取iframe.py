#coding=utf-8


from selenium import webdriver
import time
def main():
    dri = webdriver.Chrome()
    dri.get("https://www.douban.com/")

    #切换到子框架
    dri.switch_to.frame(dri.find_element_by_tag_name('iframe'))
    #先点击账号密码登录的按钮
    dri.find_element_by_xpath('/html/body/div[1]/div[1]/ul[1]/li[2]').click()
    time.sleep(3)
    dri.find_element_by_id("username").send_keys("15193252279")
    dri.find_element_by_id("password").send_keys("930819@lg")

    time.sleep(3)

    dri.find_element_by_class_name('account-form-field-submit ').click()


    time.sleep(12)
    dri.close()



if __name__ == '__main__':
    main()