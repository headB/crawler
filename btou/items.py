# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BtouItem(scrapy.Item):
    # define the fields for your item here like:
     name = scrapy.Field()
     level= scrapy.Field()
     info = scrapy.Field()

class ItcastItem(scrapy.Item):
    title = scrapy.Field()    
    h1 = scrapy.Field()    
    h2 = scrapy.Field()    
    h3 = scrapy.Field()    
