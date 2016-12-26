# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from SPIDER.items import Article

class WikiSpider(scrapy.Spider):
    name = "wiki"
    allowed_domains = ["wiki.com"]
    start_urls = ['http://en.wikipedia.org/wiki/Main_Page', 'https://en.wikipedia.org/wiki/Python']

    def parse(self, response):
        item = Article()
        title = response.xpath('//h1/text()')[0].extract()
        item['title'] = title
        print item
        return item