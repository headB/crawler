# -*- coding: UTF-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider,Rule
from btou.items import ItcastItem
class ItcastSpider(CrawlSpider):
   name = "itcast"
   siteUrl = 'xx'
   

   def __init__(self,category=None,*args,**kwargs):
    self.rules = [Rule(LinkExtractor(allow=r"/%s" %category),'parse_item')]
    super(ItcastSpider,self).__init__(*args,**kwargs)
    self.start_urls = ["http://www.itcast.cn/","http://www.520it.com"]



   def parse_item(self,response):

	 title = response.xpath("//title")
	 items = ItcastItem()
	 items['title'] = title.xpath('text()').extract()

	 h1 = response.xpath("//meta[contains(@name,'keywords')]/@content")
	 #h2 = response.xpath("//h2/p/text()").extract()
	 h2 = response.xpath("//h2/text()")
	 str = 'C' 
         if h2:
	   y = h2
	   print(y)
           for x in y.extract():
		global str
		str = str+x
		
	 if not h2:
	   print("!!!!!!!!!!!!!!!!!")
	   h2 = 'kumanxuan'
	 items['h1'] = h1.extract()
	 items['h2'] = str

	 return items
