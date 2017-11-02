from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider,Rule
from btou.items import ItcastItem
class ItcastSpider(CrawlSpider):
   name = "itcast"
   allowed_domains = ["itcast.cn"]
   start_urls = ["http://www.itcast.cn/"]
   rules = [Rule(LinkExtractor(allow=r"/subject/*"),'parse_item')]
 
   def parse_item(self,response):

	#for page in response:
	# title = page.xpath("//title").extract()
	# print(title)

        titles = response.xpath("//title")
	for title in titles:
	 items = ItcastItem()
	 items['title'] = title.xpath('text()').extract()
	 return items
