# -*- coding: utf-8 -*-
import scrapy


class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['www.ccgp.gov.cn']
    start_urls = ['http://www.ccgp.gov.cn/']

    def parse(self, response):
        pass
