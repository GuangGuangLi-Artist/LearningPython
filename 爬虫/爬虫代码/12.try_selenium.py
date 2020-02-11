#coding=utf-8


from selenium import webdriver
import time


def main():
    # driver = webdriver.Chrome()
    driver = webdriver.PhantomJS()

    #设置窗口大小
    # driver.set_window_size(height=1920,width=1080)
    #最大化窗口
    driver.maximize_window()

    driver.get("http://www.baidu.com")

    #进行页面截屏
    driver.save_screenshot("./baidu.png")


    # driver.find_element_by_id("kw").send_keys("豆瓣")
    #
    # driver.find_element_by_id("su").click()

    #获取html字符串
    print(driver.page_source)


    print(driver.current_url)

    # 获取cookies
    cookies = driver.get_cookies()
    print(cookies)
    print("*" * 100)
    cookies = {i["name"]:i["value"] for i in cookies}
    print(cookies)


    time.sleep(3)
    driver.quit()


if __name__ == '__main__':
    main()