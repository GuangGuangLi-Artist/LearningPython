# -*- coding: utf-8 -*-
import scrapy
from yangguang.items import YangguangItem

class YgSpider(scrapy.Spider):
    name = 'yg'
    allowed_domains = ['sun0769.com']
    start_urls = ['http://wz.sun0769.com/index.php/question/questionType?type=4&page=0']

    def parse(self, response):
        tr_list = response.xpath('//div[@class= "greyframe"]/table[2]/tbody/tr/td/table/tr')
        for tr in tr_list:
            item = YangguangItem()
            item["title"] = tr.xpath('./td[2]/a[@class="news14"]/@title').extract_first()
            item["href"] = tr.xpath('./td[2]/a[@class="news14"]/@href').extract_first()
            item["publish_date"] = tr.xpath('//div[@class= "greyframe"]/table[2]/tbody/tr/td/table/tbody/tr/td[@class="t12wh"]/text()').extract_first()

            yield scrapy.Request(
                item["href"],
                callback=self.parse_detail,
                meta={"item":item}
            )

            next_url = response.xpath("//a[text()='>']/@href").extract_first()
            if next_url is not None:
                yield scrapy.Request(
                    next_url,
                    callback=self.parse
                )

    def parse_detail(self,response):
        item = response.meta["item"]
        item ["content"] = response.xpath('/html/body/div[9]/table[2]/tbody/tr[1]/td').extract()
        item["content_img"] = response.xpath('/html/body/div[9]/table[2]/tbody/tr[1]/td/div[1]//img/@src').extract()
        item["content_img"] = ["http://sun0769.com" + i for i in item["content_img"]]
        print(item)



