#coding=utf-8
import requests


class TiebaSpider():
    def __init__(self,tieba_name):
        self.tieba_name = tieba_name
        self.url_temp = "https://tieba.baidu.com/f?kw=" + tieba_name + "&ie=utf-8&pn={}"
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                                      "Chrome/79.0.3945.130 Safari/537.36"}

    def get_url_list(self):
        url_list = []
        for i in range(1000):
            url_list.append(self.url_temp.format(i * 50))
        return url_list

    def parse_url(self,url):
        print(url)
        res = requests.get(url,headers=self.headers)
        return res.content.decode()

    def save_html(self,html_str,page_num):
        file_path = "{}-{}页.html".format(self.tieba_name,page_num)
        with open(file_path,"w",encoding="utf-8") as file:
            file.write(html_str)




    #实现主要逻辑
    def run(self):
        #1.构造url列表
        url_list = self.get_url_list()


        #2.遍历，发送请求，获取响应
        for url in url_list:
            html_str = self.parse_url(url)
            page_num = url_list.index(url) + 1 #页码数
            # 3.保存数据
            self.save_html(html_str,page_num)



if __name__ == "__main__":
    tieba_spider = TiebaSpider("迷男方法")
    tieba_spider.run()