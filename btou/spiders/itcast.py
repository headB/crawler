from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider,Rule
from btou.items import ItcastItem
class ItcastSpider(CrawlSpider):
   name = "itcast"
   url = 'xx' 
   def __init__(self,url=None):
    super(ItcastSpider,self).__init__()
    print(self.url)
    print("kumanxuan")
    self.url=url
    print(self.url)
    print("this is new ???")
    print(self.url)
    #self.allowed_domains = ["itcast.cn"]
    #self.start_urls = ["http://www.itcast.cn/"]
    #rules = [Rule(LinkExtractor(allow=r"/subject/*"),'parse_item')]
    #	print(category)
    #print("kumanxuan")
#	self.parsexx=category 

   #allowed_domains = ["itcast.cn"]
   
   start_urls = ["http://www.itcast.cn/"]
   rules = [Rule(LinkExtractor(allow=r"/subject/*"),'parse_item')]   
   print("this is new url or not??")
   print(url)

   def parse_item(self,response):

	 title = response.xpath("//title")
	 items = ItcastItem()
	 items['title'] = title.xpath('text()').extract()

	 h1 = response.xpath("//meta[contains(@name,'keywords')]/@content")
	 items['h1'] = h1.extract()

	 return items
