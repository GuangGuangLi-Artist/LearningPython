#coding=utf-8

from selenium import webdriver
import time

class DouyuSpider():
    def __init__(self):
        self.start_url = "https://www.douyu.com/directory/all"
        self.driver = webdriver.Chrome()

    def get_content_list(self):
        li_list = self.driver.find_elements_by_xpath('//ul[@class="layout-Cover-list"]/li')
        content_list = []
        for li in li_list:
            item = {}
            item["room_img"] = li.find_elements_by_xpath('//*[@id="listAll"]/section[1]/div[2]/ul/li[1]/div/a[1]/div[1]/div[1]/img').getattribute("src")
            item["room_title"] = li.find_elements_by_xpath('//*[@id="listAll"]/section[1]/div[2]/ul/li[1]/div/a[1]/div[2]/div[1]/h3').getattribute("title")
            item["room_cate"] = li.find_elements_by_xpath('//*[@id="listAll"]/section[1]/div[2]/ul/li[1]/div/a[1]/div[2]/div[1]/span').text
            item["anchor_name"] = li.find_elements_by_xpath('//*[@id="listAll"]/section[1]/div[2]/ul/li[1]/div/a[1]/div[2]/div[2]/h2').text
            item["watch_unm"] = li.find_elements_by_xpath('//*[@id="listAll"]/section[1]/div[2]/ul/li[1]/div/a[1]/div[2]/div[2]/span').text
            print(item)
            content_list.append(item)

            #获取下一页的元素
            next_url = self.driver.find_elements_by_xpath('//*[@id="listAll"]/section[2]/div[2]/div/ul')
            next_url = next_url[0] if len(next_url)>0 else None

            return content_list,next_url

    def save_content_list(self,content_list):
        pass



    def run(self):
        #strat_url
        #2发送请求，获取响应
        self.driver.get(self.start_url)
        #3提取数据，提取下一页的元素
        content_list,next_url = self.get_content_list()

        self.save_content_list()

        while next_url is not None:
            next_url.click()
            time.sleep(3)
            content_list,next_url = self.get_content_list()
            self.save_content_list(content_list)





if __name__ == '__main__':
    douyu = DouyuSpider()
    douyu.run()