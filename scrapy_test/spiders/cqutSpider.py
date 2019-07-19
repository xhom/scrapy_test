# coding=UTF-8

import re
from scrapy import Spider,Request
from scrapy.loader import ItemLoader
from scrapy_test.items import cqutItem

# 腾讯社招爬虫主程
class cqutSpider(Spider):
    url = "https://www.cqut.edu.cn/index/"
    pageNo = 123
    pageSize = 20

    # 爬虫名称，唯一不可重复
    name = "cqut_spider"
    # 爬虫的作用范围
    allowed_domains = ['www.cqut.edu.cn']
    # 起始url
    start_urls = [url+"xxyw.htm"]

    # override结果解析
    def parse(self, response):
        newsList = response.xpath('//div[@class="linklist1"]/ul/li')[0:self.pageSize]
        for news in newsList:
            item = cqutItem()
            item['title'] = news.xpath('./a/text()').extract()[0]
            item['link'] = news.xpath('./a/@href').extract()[0]
            item['publish_time'] = news.xpath('./span/text()').extract()[0]

            # itemLoader提供了许多有趣的方式整合数据、格式化数据、清理数据
            itemLoader = ItemLoader(item=item, response=response)
            #itemLoader.add_xpath('publish_time','./span/text()')

            item['link'] = "https://www.cqut.edu.cn/" + str(item['link']).replace("../", '')
            yield Request(item['link'], meta={'item':item}, callback=self.content_parse)

        if self.pageNo > 1:
            self.pageNo -= 1
            nextUrl = self.url+"xxyw/"+str(self.pageNo)+'.htm'
            yield Request(nextUrl,callback=self.parse)

    def content_parse(self, response):
        item, content = response.meta['item'], ''
        p_list = response.xpath('//div[@class="contentarea"]/div[@class="context"]//text()').extract()
        for p_item in p_list:
            content += p_item

        item['content'] = content

        return item


# 执行这个爬虫：scrapy crawl cqut_spider