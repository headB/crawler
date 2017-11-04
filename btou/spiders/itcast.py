from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider,Rule
from btou.items import ItcastItem
class ItcastSpider(CrawlSpider):
   name = "itcast"
   parsexx = 'xx' 
   def __init__(self,category=None):
    super(ItcastSpider,self).__init__()
    print("kumanxuan")
    print(category)
    #self.allowed_domains = ["itcast.cn"]
    #self.start_urls = ["http://www.itcast.cn/"]
    #rules = [Rule(LinkExtractor(allow=r"/subject/*"),'parse_item')]
    #	print(category)
    #print("kumanxuan")
#	self.parsexx=category 

   allowed_domains = ["itcast.cn"]
   start_urls = ["http://www.itcast.cn/"]
   rules = [Rule(LinkExtractor(allow=r"/subject/*"),'parse_item')]   
   print(parsexx)

   def parse_item(self,response):

	 title = response.xpath("//title")
	 items = ItcastItem()
	 items['title'] = title.xpath('text()').extract()

	 h1 = response.xpath("//meta[contains(@name,'keywords')]/@content")
	 items['h1'] = h1.extract()

	 return items
