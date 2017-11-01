# -*- coding: utf-8 -*-
import scrapy
from btou.items import BtouItem
import re

class SeemygoSpider(scrapy.Spider):
    name = 'seemygo'
    allowed_domains = ['520it.com']
    start_urls = ['http://520it.com/teacher']

    def parse(self, response):
        filename = "teacher.html"
        #with open(filename,'w') as f:
        # f.write(response.body)
	
        items = []
	for each in response.xpath("//li[@class='t']"):
	#for each in response.xpath("//li[contains(@class,'t')]/@class"):
	 #print(each.extract())
	 item = BtouItem()
	 item['name'] = each.xpath("h1/em/text()").extract()
	 item['level'] = each.xpath("h1/span/text()").extract()
	 #item['info']  = each.xpath("span/p/text()").extract()
	 infoArray  = each.xpath("span").re_first(r'>.+<')
	 test = re.sub(r'<.*?>|<|>','',infoArray)
	 item['info'] = test
	 info = each.xpath("span/p/text()").extract()
	 if not info:
	 # print("这里为空啊~~~~~~~~,请你自己采取措施！！")
	  item['info']  = each.xpath("span/p/span/text()").extract()
	  info1 = each.xpath("span/p/span/text()").extract()
	  if not info1:
	     item['info']  = each.xpath("span/p/span/span/text()").extract()
	 #print(each.xpath("h1/em/text()").extract())
	 yield item
