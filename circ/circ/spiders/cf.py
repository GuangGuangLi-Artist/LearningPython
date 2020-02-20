# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import re

class CfSpider(CrawlSpider):
    name = 'cf'
    allowed_domains = ['circ.gov.cn']
    start_urls = ['http://bxjg.circ.gov.cn/web/site0/tab5240/module14430/page1.htm']


    #定义提取url规则
    rules = (
        #LinkExtractor 链接提取器，提取url地址
        #callback 提取出来的url地址的response会交给callback处理
        #follow 当前url地址的响应是够重新进过rules来提取的url地址
        Rule(LinkExtractor(allow=r'/web/site0/tab5240/info\d+\.htm'), callback='parse_item'),
        Rule(LinkExtractor(allow=r'/web/site0/tab5240/module14430/page\d+\.htm'), follow=True),


    )

    def parse_item(self, response):
        item = {}
        item['title'] = re.findall("<!--TitleStart-->(.*?)<!--TitleEnd-->",response.body.decode())[0]
        item['data'] = re.findall("发布时间：(20\d{2}-\d{2}-\d{2})",response.body.decode())[0]
        print(item)
        # return item
