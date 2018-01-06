# -*- coding: UTF-8 -*-

import scrapy
from gov.items import GovItem

class BeginSpider(scrapy.Spider):
    name="begin"

    prefix='http://search.ccgp.gov.cn/bxsearch?searchtype=2&page_index='
    page_index='1'
    suffix='&bidSort=0&buyerName=&projectId=&pinMu=0&bidType=0&dbselect=bidx&kw=%E5%8C%BB%E6%83%A0%E7%A7%91%E6%8A%80&start_time=2017%3A10%3A06&end_time=2018%3A01%3A06&timeType=4&displayZone=&zoneId=&pppStatus=0&agentName='
   # start_urls=['http://search.ccgp.gov.cn/bxsearch?searchtype=2&page_index=1&bidSort=&buyerName=&projectId=&pinMu=&bidType=&dbselect=bidx&kw=%E5%8C%BB%E6%83%A0%E7%A7%91%E6%8A%80&start_time=2017%3A09%3A21&end_time=2017%3A12%3A22&timeType=4&displayZone=&zoneId=&pppStatus=0&agentName=',]
    start_urls=[prefix+page_index+suffix,]
    def parse(self,response):
        filename='home.html'

        for project in response.css('ul.vT-srch-result-list-bid').css("li"):
            project_name=project.css("a::text").extract()[0].strip()
            province=project.css("a::text").extract()[1].strip()
            money_url=project.css("li").css("a::attr(href)").extract_first()
            #yield response.follow(money_url,self.parse_money)
            item = GovItem()
            item['name']=project_name
            item['pro']=province
            request=response.follow(money_url,self.parse_money)
            request.meta['item'] = item
            yield request
            """
            yield{
                'project_name':project_name,
                'province':province,
                'money':money,
            }
            """
        prefix='http://search.ccgp.gov.cn/bxsearch?searchtype=2&page_index='
        suffix='&bidSort=&buyerName=&projectId=&pinMu=&bidType=&dbselect=bidx&kw=%E5%8C%BB%E6%83%A0%E7%A7%91%E6%8A%80&start_time=2017%3A09%3A21&end_time=2017%3A12%3A22&timeType=4&displayZone=&zoneId=&pppStatus=0&agentName='
        next_page=prefix+str(3)+suffix
        if next_page is not None:
            yield response.follow(next_page,callback=self.parse)
    #    x=response.css("p.pager")

    def parse_money(self,response):
        item = response.meta['item']
        item['money'] = response.css('div.table').css('table').css('tr')[7].css('td::text')[1].extract()
        item['company'] = response.css('div.table').css('table').css('tr')[3].css('td::text')[1].extract()
        item['date'] = response.css('div.table').css('table').css('tr')[4].css('td::text')[3].extract()
        yield item
        """
         yield{

                'fan':20,
         }
        """
