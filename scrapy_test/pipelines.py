# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ScrapyTestPipeline(object):
    def process_item(self, item, spider):
        return item

import json
from scrapy_test.db.db_save import DBSave
class cqutPipeline(object):
    # 功能： 保存item数据

    def __init__(self):
        self.save_file = open("cqut_news.json", "w")
        self.dbSave = DBSave("cqut_news")

    def process_item(self, item, spider):
        #json_item = json.dumps(dict(item), ensure_ascii=False) + ",\n"
        #self.save_file.write(json_item.encode("gbk"))
        #保存到数据库
        self.dbSave.insert(item)
        return item

    def close_spider(self, spider):
        self.save_file.close()
        self.dbSave.close_conn()