# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item,Field

# cqut-news-数据模型
class cqutItem(Item):
    # 新闻标题
    title        = Field()
    # 链接
    link         = Field()
    # 内容(通过子链接link抓取)
    content      = Field()
    # 发布时间
    publish_time = Field()