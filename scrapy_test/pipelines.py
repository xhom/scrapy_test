# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ScrapyTestPipeline(object):
    def process_item(self, item, spider):
        return item

class txszPipeline(object):
    # 功能： 保存item数据

    def __init__(self):
        pass

    def process_item(self, item, spider):
        print 'item:',item

    def close_spider(self, spider):
        pass