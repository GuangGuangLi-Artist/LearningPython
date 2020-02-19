# -*- coding: utf-8 -*-
import scrapy
import logging

logger = logging.getLogger(__name__)


class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.cn'] #允许爬取的范围
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml'] #最开始请求的starturl地址

    def parse(self, response):
        #处理start_url对应的响应
        # ret = response.xpath("//div[@class='tea_con']//h3/text()").extract()
        # print(ret)


        #分组
        # li_list = response.xpath("//div[@class='tea_con']//li")
        # for li in li_list:
        #     item = {}
        #     item['name'] = li.xpath(".//h3/text()").extract_first()
        #     item['title'] = li.xpath(".//h4/text()").extract_first()
        #     yield item  #yiled的作用是防止内存占用过度

        for i in range(10):
            item = {}
            item["come_from"] = "itcast"
            logger.warning(item)
            yield item

