# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyTestItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

# cqut-news-数据模型
class cqutItem(scrapy.Item):
    # 新闻标题
    title       = scrapy.Field()
    # 链接
    link        = scrapy.Field()
    # 内容(通过子链接link抓取)
    content     = scrapy.Field()
    # 发布时间
    publishTime = scrapy.Field()