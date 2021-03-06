# -*- coding: UTF-8 -*-

import scrapy

from gov.items import GovItem

class BeginSpider(scrapy.Spider):
    name="begin2"

    prefix='http://search.ccgp.gov.cn/bxsearch?searchtype=2&page_index='
    page_index='1'
    suffix='&bidSort=&buyerName=&projectId=&pinMu=&bidType=&dbselect=bidx&kw=%E5%8C%BB%E6%83%A0%E7%A7%91%E6%8A%80&start_time=2017%3A09%3A21&end_time=2017%3A12%3A22&timeType=4&displayZone=&zoneId=&pppStatus=0&agentName='
   # start_urls=['http://search.ccgp.gov.cn/bxsearch?searchtype=2&page_index=1&bidSort=&buyerName=&projectId=&pinMu=&bidType=&dbselect=bidx&kw=%E5%8C%BB%E6%83%A0%E7%A7%91%E6%8A%80&start_time=2017%3A09%3A21&end_time=2017%3A12%3A22&timeType=4&displayZone=&zoneId=&pppStatus=0&agentName=',]
    start_urls=[prefix+page_index+suffix,]
    def parse(self,response):
        filename='home.html'
        items=[]
        for project in response.css('ul.vT-srch-result-list-bid').css("li"):

            item = GovItem()
            item['name']=project.css("a::text").extract()[0]
            item['pro']=project.css("a::text").extract()[1]
            item['info']=project.css("p::text").extract()
            items.append(item)

        #prefix='http://search.ccgp.gov.cn/bxsearch?searchtype=2&page_index='
        #suffix='&bidSort=&buyerName=&projectId=&pinMu=&bidType=&dbselect=bidx&kw=%E5%8C%BB%E6%83%A0%E7%A7%91%E6%8A%80&start_time=2017%3A09%3A21&end_time=2017%3A12%3A22&timeType=4&displayZone=&zoneId=&pppStatus=0&agentName='
        #next_page=prefix+str(2)+suffix
        #if next_page is not None:
        #    yield response.follow(next_page,callback=self.parse)
        return items

