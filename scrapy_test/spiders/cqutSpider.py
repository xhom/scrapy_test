# coding=UTF-8

import scrapy
from scrapy_test.items import cqutItem

# 腾讯社招爬虫主程
class cqutSpider(scrapy.Spider):
    url = "https://www.cqut.edu.cn/index/"
    pageSize = 123

    # 爬虫名称，唯一不可重复
    name = "cqut_spider"
    # 爬虫的作用范围
    allowed_domains = ['www.cqut.edu.cn']
    # 起始url
    start_urls = [url+"xxyw.htm"]

    # override结果解析
    def parse(self, response):
        item = cqutItem()
        newsList = response.xpath('//div[@class="linklist1"]/ul/li')
        for news in newsList:
            item['title'] = news.xpath('./a/text()').extract()[0]
            item['link'] = news.xpath('./a/@href').extract()[0]
            item['publishTime'] = news.xpath('./span/text()').extract()[0]

            detailUrl = "https://www.cqut.edu.cn/" + str(item['link']).replace("../", '')
            yield scrapy.Request(detailUrl, meta={'item':item}, callback=self.content_parse)

        if self.pageSize > 122:
            self.pageSize -= 1

        nextUrl = self.url+"xxyw/"+str(self.pageSize)+'.htm'
        yield scrapy.Request(nextUrl,callback=self.parse)

    def content_parse(self, response):
        item = response.meta['item']
        content = ''
        content_list = response.xpath('//div[@class="contentarea"]/div[@class="context"]/div/p/text()').extract()
        for content_item in content_list:
            content += content_item
        item['content'] = content

        yield item


# 执行这个爬虫：scrapy crawl cqut_spider