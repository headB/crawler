# -*- coding: utf-8 -*-
#import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from btou.items import BtouItem

class SeemygoSpider(CrawlSpider):
    name = 'seemygo'
    allowed_domains = ['520it.com']
    start_urls = ['http://520it.com/']
    rules = [Rule(LinkExtractor(allow=r"/special/*"),'parse_itemxx')]

    def parse_itemxx(self,response):
     sites = response.xpath('//title')
     items = []
     content = []
     for site in sites:
      item = BtouItem()
      item['name'] = site.xpath('text()').extract()
      items.append(item)
      yield item 
	
	 #print(each.extract())
	 #item = BtouItem()
	 #item['name'] = each.xpath("h1/em/text()").extract()
	 #item['level'] = each.xpath("h1/span/text()").extract()
	 
	 #infoArray  = each.xpath("span").re_first(r'>.+<')
	 #test = re.sub(r'<.*?>|<|>','',infoArray)
	 #item['info'] = test
	 #info = each.xpath("span/p/text()").extract()
	 #if not info:
	 # item['info']  = each.xpath("span/p/span/text()").extract()
	 # info1 = each.xpath("span/p/span/text()").extract()
	 # if not info1:
	 #    item['info']  = each.xpath("span/p/span/span/text()").extract()
	 #yield item
