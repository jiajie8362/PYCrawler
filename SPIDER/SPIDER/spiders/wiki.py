# -*- coding: utf-8 -*-
from scrapy.contrib.spiders import CrawlSpider, Rule
from SPIDER.items import Article
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor

from SPIDER.items import Article

class WikiSpider(CrawlSpider):
    name = "wiki"
    allowed_domains = ["en.wikipedia.org"]
    start_urls = ['http://en.wikipedia.org/wiki/Main_Page', 'https://en.wikipedia.org/wiki/Python']
    rules = [Rule(SgmlLinkExtractor(allow=('(/wiki/).*$'),), callback='parse', follow=True)]

    def parse(self, response):
        item = Article()
        title = response.xpath('//h1/text()')[0].extract()
        item['title'] = title
        print item
        return item


        