# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GovItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    money = scrapy.Field()
    pro  = scrapy.Field()
    company=scrapy.Field()
    date=scrapy.Field()
    
