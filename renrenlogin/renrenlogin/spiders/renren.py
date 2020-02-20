# -*- coding: utf-8 -*-
import scrapy
import re

class RenrenSpider(scrapy.Spider):
    name = 'renren'
    allowed_domains = ['renren.com']
    start_urls = ['http://www.renren.com/526950701/profile']


    def start_requests(self):
        cookies = "_r01_=1; anonymid=k69b1p5534vj36; taihe_bi_sdk_uid=13bb78ae5a7b53b3b824c20d92d39b72; ln_uact=940102569@qq.com; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; jebe_key=0750826c-3ade-451f-9c16-af4574c25b45%7C1c7c11a4c02283afc788950c9fcff0d8%7C1580906796560%7C1%7C1580906795565; __gads=ID=009d129daa5ed655:T=1580907068:S=ALNI_MbrAIjhqHpd4A_DSE86P1mBP46X7Q; wp=0; _de=7BC63459E74EF7A6E2A69D838E8B6F33696BF75400CE19CC; depovince=ZGQT; jebecookies=76a267eb-4622-420c-b24b-8eac4fb315b4|||||; ick_login=b2b0ee03-1b1d-4308-9725-a85b42872f9c; taihe_bi_sdk_session=131b5c9f86119eb62e155fa7d110467d; p=3850e120e518c95ab0d6a8278602303a1; ap=526950701; first_login_flag=1; t=7f4c7270e98723c598707b7da8831a5a1; societyguester=7f4c7270e98723c598707b7da8831a5a1; id=526950701; xnsid=9d73aaec; ver=7.0; loginfrom=null; wpsid=15820644056550; vip=1; wp_fold=0"
        cookies = {i.split("=")[0]:i.split("=")[1] for i in cookies.split("; ")}
        yield scrapy.Request(
            self.start_urls[0],
            callback=self.parse,
            cookies=cookies
        )

    def parse(self, response):
        print(re.findall("李广", response.body.decode()))
        yield scrapy.Request(
            "http://www.renren.com/526950701/profile?v=info_timeline",
            callback=self.parse_detail
        )

    def parse_detail(self,response):
        print(re.findall("李广", response.body.decode()))

