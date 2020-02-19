# -*- coding: utf-8 -*-
import scrapy
from tencent.items import TencentItem


class HrSpider(scrapy.Spider):
    name = 'hr'
    allowed_domains = ['tencent.com']
    start_urls = ['https://careers.tencent.com/position.php']

    def parse(self, response):
        div_list = response.xpath('//div[@class="recruit-wrap recruit-margin"]/div')
        for div in div_list:
            item = {}
            item["title"] = div.xpath('./a/h4/text()').extract_first()
            item["position"] = div.xpath('./a/p/span[3]/text()').extract_first()
            item["publish_data"] = div.xpath('./a/p/span[4]/text()').extract_first()
            yield item


            next_url = response.xpath("//div[@class='page-number']/ul/li/span[@class='page-text']").extract_first()
            if next_url !="javascript;;":
                next_url = "http://hr.tencent.com/" + next_url
                yield scrapy.Request(
                    next_url,
                    callback=self.parse1,
                    meta={"item":item}
                )

    def parse1(self,response):
        response.meta["item"]