# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from tencent.items import TencentItem

from pymongo import MongoClient
client = MongoClient()
collection = client["tencent"]["hr"]
class TencentPipeline(object):
    def process_item(self, item, spider):
        if isinstance(item,TencentItem):
            print(item)
            collection.insert(dict(item))
        return item
