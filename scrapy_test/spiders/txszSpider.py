# coding=UTF-8

import scrapy
from scrapy_test.items import txszItem

class txszSpider(scrapy.Spider):
    url = "http://hr.tencent.com/position.php?&start="
    offset = 0

    # 爬虫名称，唯一不可重复
    name = "txsz_spider"
    # 爬虫的作用范围
    allowed_domains = ['tencent.com']
    # 起始url
    start_urls = [url+str(offset)]
    # override结果解析
    def parse(self, response):
        print response



# 执行这个爬虫：scrapy crawl txsz_spider