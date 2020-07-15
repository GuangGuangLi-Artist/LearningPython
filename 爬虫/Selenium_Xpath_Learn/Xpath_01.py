#coding=utf-8


from selenium import webdriver
import time

def run():
    driver = webdriver.Chrome()
    driver.get('http://www.baidu.com')
    time.sleep(2)



if __name__ == '__main__':
    run()